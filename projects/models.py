from django.db import models


class Project(models.Model):
    ptitle = models.CharField(max_length=100)
    pdescription = models.TextField()
    ptechnology = models.CharField(max_length=20)
    pimage = models.FilePathField(path="/img")
