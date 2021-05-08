from django.db import models

# Create your models here.
class Password(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    url = models.URLField()
    notes = models.TextField()

    def __str__(self):
        return self.name