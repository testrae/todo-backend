from . import models
from . import serializers
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


#ToDo model api interface
class ToDoViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = models.ToDoItem.objects.all()
        serializer = serializers.ToDoItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = models.ToDoItem.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ToDoItemSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
