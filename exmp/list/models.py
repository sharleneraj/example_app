from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phonenum = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

