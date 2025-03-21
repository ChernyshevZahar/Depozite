from django.db import models

class Wallet(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)