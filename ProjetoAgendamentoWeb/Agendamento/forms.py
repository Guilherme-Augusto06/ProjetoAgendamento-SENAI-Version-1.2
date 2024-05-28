from django import forms
from .models import Salas

class formCadastroUsuario(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40)
    last_name = forms.CharField(label="Sobrenome", max_length=40)
    user = forms.CharField(label="Usuário", max_length=40)   
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuario", max_length=40)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormAgendarSala(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=40)
    last_name = forms.CharField(label="Sobrenome", max_length=40)
    user = forms.CharField(label="Usuário", max_length=40)
    email = forms.EmailField(label="Email", max_length=100)
    dataAgendamento = forms.DateField(label="Data de agendamento", widget=forms.DateInput(attrs={'type': 'date'}))
    salas = forms.ModelChoiceField(queryset=Salas.objects.all())

