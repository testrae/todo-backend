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
        self.assertEqual(item.text, "Ev işleri yapılacak")



class Tests(APITestCase):


    def create_model(self):
        data = {'text': 'Ev işleri yapılacak','done': False }
        item = ToDoItem(**data).save()

    def test_create(self):
        """
        Test Create Method
        """
        data = {'text': 'Ev işleri yapılacak','done': False }
        response = self.client.post(reverse('rest:ToDoItem-list'),data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDoItem.objects.count(), 1)
        self.assertEqual(ToDoItem.objects.get().text, 'Ev işleri yapılacak')

    def test_get_todo(self):
        """
        Test Get Method
        """
        self.create_model()
        response = self.client.get(reverse('rest:ToDoItem-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'text': 'Ev işleri yapılacak','done': False }])