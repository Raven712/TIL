from django.db import models

# Create your models here.

class mo_re(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


