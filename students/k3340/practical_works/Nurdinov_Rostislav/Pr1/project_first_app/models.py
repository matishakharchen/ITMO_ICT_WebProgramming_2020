from django.db import models
from django.urls import reverse


class Auto(models.Model):
    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    gos_number = models.CharField(max_length=50)


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    members = models.ManyToManyField(Auto, through='Ownership')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class AdditionalData(models.Model):
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, primary_key=True)
    passport_num = models.CharField(max_length=50)
    home_address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)


class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    data_start_owner = models.DateField()
    data_finish_owner = models.DateField()


class License(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=50)
    type_license = models.CharField(max_length=50)
    date_license = models.DateField()
