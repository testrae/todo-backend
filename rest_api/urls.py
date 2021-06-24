from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from . import api
from . import views
from rest_framework.routers import DefaultRouter

app_name='rest'
router = DefaultRouter()
router.register(r'ToDoItem', api.ToDoViewSet, basename='ToDoItem')
urlpatterns = router.urls

urlpatterns = (
    path('v1/', include(router.urls), name='rest'),
)


