from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.title
