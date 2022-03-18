from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:aluno_ra_aluno>', views.aluno, name='aluno')
]