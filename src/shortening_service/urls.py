from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:generated_id>', views.redirect, name='redirect'),
    path('links', views.generate_link, name="generate_link")
]
