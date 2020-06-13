from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(null=False,max_length=50)
    age = models.IntegerField(null=False,default=0)

    def __str__(self):
        return f'{self.name} {self.age}'