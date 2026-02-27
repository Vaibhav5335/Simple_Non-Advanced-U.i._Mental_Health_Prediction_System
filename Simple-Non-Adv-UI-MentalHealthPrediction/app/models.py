from django.db import models


class candidate(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(null=False, max_length=20)
    name = models.CharField(null=False, max_length=20)

    
