from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    emeil = models.EmailField()

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return f'{self.title} {self.created_date}'

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    text = models.CharField(null=False, max_length=250)
    published_date = models.DateTimeField(default=timezone.now)