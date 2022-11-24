# urls.py
from django.urls import path
from .views import PersonaListView

urlpatterns = [
    path('personas/', PersonaListView.as_view()),
]