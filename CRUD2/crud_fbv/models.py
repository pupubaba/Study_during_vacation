from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title