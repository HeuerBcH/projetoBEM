from django import forms
from .models import Turma

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'horario_inicio', 'horario_fim', 'dias', 'professor']
    
    def clean_horario_fim(self):
        horario_inicio = self.cleaned_data.get('horario_inicio')
        horario_fim = self.cleaned_data.get('horario_fim')
        if horario_inicio and horario_fim and horario_fim <= horario_inicio:
            raise forms.ValidationError("O horário de fim deve ser posterior ao horário de início.")
        return horario_fim

    def clean_dias(self):
        dias = self.cleaned_data.get('dias')
        dias_validos = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        dias_lista = [dia.strip() for dia in dias.split(',')]
        for dia in dias_lista:
            if dia not in dias_validos:
                raise forms.ValidationError(f"O dia '{dia}' não é válido. Os dias válidos são: {', '.join(dias_validos)}.")
        return dias
