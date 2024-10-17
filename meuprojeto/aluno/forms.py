from django import forms
from .models import Aluno
from turma.models import Turma
import re
from datetime import datetime

class AlunoForm(forms.ModelForm):
    turmas = forms.ModelMultipleChoiceField(
        queryset=Turma.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    
    data_nascimento = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'dd/mm/aaaa',
            'oninput': 'formatDate(this)',
        })
    )

    class Meta:
        model = Aluno
        fields = [
            'nome_aluno', 
            'matricula',
            'data_nascimento', 
            'turmas', 
            'nome_responsavel', 
            'numero_responsavel', 
            'email_responsavel'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.data_nascimento:
            self.initial['data_nascimento'] = self.instance.data_nascimento.strftime('%d/%m/%Y')

    def clean_data_nascimento(self):
        data = self.cleaned_data['data_nascimento']
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', data):
            raise forms.ValidationError("A data deve estar no formato dd/mm/aaaa.")
        
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
        if not re.match(r'^\(\d{2}\) \d{9}$', numero) and not re.match(r'^\(\d{2}\) \d{4}-\d{4}$', numero):
            raise forms.ValidationError("Por favor, insira um número de telefone válido no formato (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.")
        return numero

    def save(self, commit=True):
        aluno = super().save(commit=False)
        aluno.colocacao_geral = 0
        
        if commit:
            aluno.save()
            aluno.turmas.set(self.cleaned_data['turmas'])
        return aluno
