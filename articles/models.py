from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
