from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class TaskImages(models.Model):
    
    image = models.ImageField(upload_to='task_images/',blank=True,null=True) 



PRIORITY = (
    ('HIGH','HIGH'),
    ('MEDIUM','MEDIUM'),
    ('LOW','LOW')
)
class TaskModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True) 
    title = models.CharField(max_length=100) 
    desc = models.TextField(blank=True) 
    priority = models.CharField(max_length=7,choices=PRIORITY,default='MEDIUM')
    image = models.ManyToManyField(TaskImages,blank=True,null=True) 
    is_complete = models.BooleanField(default=False) 
    created = models.DateTimeField(default=timezone.now()) 
    updated = models.DateField(auto_now=True) 


    def __str__(self):
        return f'{self.title}' 
    class Meta:
        ordering = ['-priority', 'created']
