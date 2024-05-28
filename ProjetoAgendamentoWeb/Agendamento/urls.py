from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),         # Inclui as urls do app blog
    path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
    path('login', views.login, name='login'),
    path('faq', views.faq, name="faq"),
    path('faqAdmin', views.faqAdmin, name="faqAdmin"),
    path('homepageAdmin', views.homepageAdmin, name='homepageAdmin'),
    path('logout', views.logout_view, name='logout'),

]