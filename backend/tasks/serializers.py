from rest_framework import serializers 
from .models import TaskModel, TaskImages

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImages
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    image = TaskImageSerializer(many=True,required=False)
    class Meta:
        model = TaskModel
        fields = '__all__' 

        