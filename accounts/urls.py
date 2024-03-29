from django.urls import path
from .views import user_createview, user_detailview

urlpatterns = [
    path('signup/', user_createview, name='signup'),
    path('profile/<int:pk>/', user_detailview, name='user-detail'),
]