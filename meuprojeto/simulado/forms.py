from django import forms
from .models import Simulado
from turma.models import Turma  # Importa o modelo Turma

class SimuladoForm(forms.ModelForm):
    turma = forms.ModelChoiceField(queryset=Turma.objects.all(), label="Turma", required=True)

    class Meta:
        model = Simulado
        fields = ['nome', 'materia', 'data_inicio', 'turma']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'materia': forms.Select(choices=Simulado.MATERIA_CHOICES, attrs={'class': 'form-control'}),
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'turma': forms.Select(attrs={'class': 'form-control'})
        }
