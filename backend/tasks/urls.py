from django.urls import path, include 
from .views import * 
from rest_framework.routers import DefaultRouter 
router = DefaultRouter()
router.register('tasks',TaskView,basename='task') 

urlpatterns = [
    path('',include(router.urls)),
    path('complete/<int:id>/',CompleteTask.as_view(),name='complete'),

]