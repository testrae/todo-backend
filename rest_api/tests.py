from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ToDoItem
from django.test import TestCase

class ModelTests(TestCase):

    def test_create_model_ToDo(self):
        data = {'text': 'Ev işleri yapılacak','done': False }
        item = ToDoItem(**data).save()
        item = ToDoItem.objects.get(text="Ev işleri yapılacak")
        self.assertIsInstance(item, ToDoItem)