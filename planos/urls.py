from django.urls import path

from . import views

app_name = 'planos'

urlpatterns = [
    path('planos/', views.planosView.as_view(), name='planos')
]
