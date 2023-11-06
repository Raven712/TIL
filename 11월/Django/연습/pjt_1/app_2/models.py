from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.TextField()
# 얘들을 DB로 만들려면 makemigrations으로 설계도만들고 migrate로 DB만듦...
# python manage.py makemigrations
# python manage.py migrate