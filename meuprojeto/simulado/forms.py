from django import forms
from .models import Simulado
from aluno.models import Aluno  # Importa o modelo Aluno do app aluno

class SimuladoForm(forms.ModelForm):
    class Meta:
        model = Simulado
        fields = ['nome', 'data_realizacao', 'materia', 'alunos_participantes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Simulado'}),
            'data_realizacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'materia': forms.Select(choices=[('Matematica', 'Matemática'), ('Portugues', 'Português')],
                                    attrs={'class': 'form-control'}),
            'alunos_participantes': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
