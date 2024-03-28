from rest_framework import generics

from .models import Todo
from .serializers import TodoSimpleSerializer


class TodosAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSimpleSerializer


todos_api_view = TodosAPIView.as_view()
