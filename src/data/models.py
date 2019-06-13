from django.db import models


class info(models.Model):
    name = models.CharField(max_length=200,blank=False) #max_field = required
    email = models.EmailField(max_length=200,blank=False)
    phone = models.CharField(max_length=10,blank=False) #blank=true(field can be left if false then it has to be filled)
    pic =   models.FileField()
    department = models.CharField(max_length=200,blank=False)

    def __str__(self):
        return self.name




