from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .models import Senai, Salas
from .forms import formCadastroUsuario, FormLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Decorator to check if user belongs to allowed groups
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User, Group
from .models import Senai, Salas
from .forms import formCadastroUsuario, FormLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Decorator to check if user belongs to allowed groups
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            # Check if user belongs to any of the specified groups
            if bool(u.groups.filter(name__in=group_names)):
                return True
        return False
    return user_passes_test(in_groups)

@login_required
@group_required('Coordenador')
def homepageAdmin(request):
    if request.user.groups.filter(name='Coordenador').exists():
        context = {}
        dadosSenai = Senai.objects.all()
        dadosSalas = Salas.objects.all()
        context["dadosSenai"] = dadosSenai
        context["dadosSalas"] = dadosSalas
        return render(request, 'homepageAdmin.html', context)
    else:
        return redirect(request, '/', context)

# Rest of your views remain unchanged


def logout_view(request):
    logout(request)
    return redirect('/')

def homepage(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    return render(request, 'homepage.html', context)

def cadastroUsuario(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = formCadastroUsuario(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['first_name']
            var_sobrenome = form.cleaned_data['last_name']
            var_usuario = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['password']

            user = User.objects.create_user(username=var_usuario, email=var_email, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.save()
            return redirect('/login')
    else:
        form = formCadastroUsuario()
        context['form'] = form
    return render(request, 'cadastroUsuario.html', context)

def login(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            var_usuario = form.cleaned_data['user']
            var_senha = form.cleaned_data['password']
            
            user = authenticate(username=var_usuario, password=var_senha)

            if user is not None:
                auth_login(request, user)
                return redirect('/homepageAdmin')
            else:
                print('Login falhou')
    else:
        form = FormLogin()
        context['form'] = form
    return render(request, 'login.html', context)

def faq(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    return render(request, 'faq.html', context)

def faqAdmin(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    return render(request, 'faqAdmin.html', context)
