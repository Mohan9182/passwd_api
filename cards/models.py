from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=200)
    card_no = models.CharField(max_length=16)
    color = models.CharField(max_length=10)
    cvv = models.CharField(max_length=3)
    expiry = models.CharField(max_length=5)

    def __str__(self):
        return self.bank_name
