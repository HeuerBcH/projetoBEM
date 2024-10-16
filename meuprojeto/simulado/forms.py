from django import forms
from .models import Simulado
from turma.models import Turma  # Importa o modelo Turma

class SimuladoForm(forms.ModelForm):
    turma = forms.ModelChoiceField(queryset=Turma.objects.all(), label="Turma", required=True)
    
    class Meta:
        model = Simulado
        fields = ['nome', 'materia', 'data_inicio', 'turma']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Simulado'}),
            'materia': forms.Select(choices=[
                ('matematica', 'Matemática'), 
                ('portugues', 'Português')
            ], attrs={'class': 'form-control'}),
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(SimuladoForm, self).__init__(*args, **kwargs)
        self.fields['turma'].queryset = Turma.objects.all()  # Exibe todas as turmas cadastradas
        self.fields['turma'].widget.attrs.update({'class': 'form-control'})
