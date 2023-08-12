from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/', views.edicionCurso),
    path('editarCurso/<str:codigo>/', views.editarCurso, name='editarCurso'),
    path('eliminarCurso/<codigo>' , views.eliminarCurso)
]