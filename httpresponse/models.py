from django.db import models


class HTMLTag(models.Model):
    html_tag = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.html_tag
