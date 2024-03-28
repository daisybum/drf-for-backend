from django.urls import path

from .views import todos_api_view

urlpatterns = [
    path('todo/', todos_api_view),
]