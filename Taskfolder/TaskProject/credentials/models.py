# from django.db import models
# from django.db.models import CASCADE
#
#
# class District(models.Model):
#     name=models.CharField(max_length=250)
#
#
#     def __str__(self):
#         return self.name
#
# class Acc_type(models.Model):
#     name=models.CharField(max_length=250)
#
#
#     def __str__(self):
#         return self.name
#
# class Details(models.Model):
#     name=models.CharField(max_length=250)
#     district=models.ForeignKey(District, on_delete=CASCADE)
#
#     def __str__(self):
#         return self.name


from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)

class register(models.Model):
        username = models.CharField(max_length=250)
        password = models.CharField(max_length=250)

class Branches(models.Model):
            name = models.CharField(max_length=250, unique=True)
            slug = models.SlugField(max_length=250, unique=True)

class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Branches, on_delete=models.CASCADE)

