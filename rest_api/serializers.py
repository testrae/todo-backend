from . import models
from django.contrib.auth.models import Group, User

from rest_framework import serializers


class ToDoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ToDoItem
        fields = (
            'text',
            'done'
        )
