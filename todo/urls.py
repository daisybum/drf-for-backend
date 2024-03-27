from django.urls import path

from .views import todo_viewset

urlpatterns = [
    path('todos/', todo_viewset),
]