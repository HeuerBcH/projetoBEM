from django import forms
from .models import Aluno
from turma.models import Turma  # Importa o modelo Turma
import re
from datetime import datetime

class AlunoForm(forms.ModelForm):
    turmas = forms.ModelMultipleChoiceField(
        queryset=Turma.objects.all(),  # Obtém todas as turmas existentes
        widget=forms.CheckboxSelectMultiple,  # Exibe as turmas como checkboxes
        required=True,  # Torna o campo obrigatório
    )
    
    data_nascimento = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'dd/mm/aaaa',
            'oninput': 'formatDate(this)',  # Chama a função de formatação
        })
    )

    class Meta:
        model = Aluno
        fields = [
            'nome_aluno', 
            'matricula',  # Checkbox, com default em True
            'data_nascimento', 
            'turmas', 
            'nome_responsavel', 
            'numero_responsavel', 
            'email_responsavel'
        ]  # Inclui os novos campos

    def clean_data_nascimento(self):
        data = self.cleaned_data['data_nascimento']
        # Verifica se a data está no formato DD/MM/YYYY
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
            raise forms.ValidationError("A data deve estar no formato dd/mm/aaaa.")
        
        # Converte a data para o formato YYYY-MM-DD para salvar no banco
        try:
            data_convertida = datetime.strptime(data, '%d/%m/%Y').date()
        except ValueError:
            raise forms.ValidationError("Data inválida.")
        
        return data_convertida

    def clean_email_responsavel(self):
        email = self.cleaned_data['email_responsavel']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Por favor, insira um email válido.")
        return email

    def clean_numero_responsavel(self):
        numero = self.cleaned_data['numero_responsavel']
        # Valida o número de telefone brasileiro com parênteses para o DDD e 9 dígitos
        if not re.match(r'^\(\d{2}\) \d{9}$', numero) and not re.match(r'^\(\d{2}\) \d{4}-\d{4}$', numero):
            raise forms.ValidationError("Por favor, insira um número de telefone válido no formato (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.")
        return numero

    def save(self, commit=True):
        aluno = super().save(commit=False)
        aluno.colocacao_geral = 0  # Define colocação como 0
        
        if commit:
            aluno.save()
            aluno.turmas.set(self.cleaned_data['turmas'])  # Associa as turmas selecionadas
        return aluno
