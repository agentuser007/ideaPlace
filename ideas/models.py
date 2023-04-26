# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Idea(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_ideas')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea_detail', args=[str(self.id)])
        
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea')

    def __str__(self):
        return f'{self.user.username} likes {self.idea.title}'        


