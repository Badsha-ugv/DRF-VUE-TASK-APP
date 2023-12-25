from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from django.views.decorators.csrf import csrf_exempt

from .models import TaskModel, TaskImages
from .serializers import TaskSerializer, TaskImageSerializer


class TaskView(ModelViewSet):
    permission_classes = [IsAuthenticated] 
    
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    def get_queryset(self):
        return TaskModel.objects.filter(user=self.request.user,is_complete=False) 
    
    def perform_create(self, serializer):
        instance=serializer.save(user=self.request.user) 

        # save image to model
        image_data = self.request.FILES.getlist('image',[])
        for img in image_data:
            instance.image.create(image=img)


class CompleteTask(APIView):
    def get(self, request,id=None):
        task = TaskModel.objects.get(id=id)
        task.is_complete = True 
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

