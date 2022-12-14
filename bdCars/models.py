from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Owner(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    name = models.CharField(max_length=20)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=50, default="")
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=False, related_name='cars')
    isFresh = models.BooleanField(default=True)
    used = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)])
    country = models.ManyToManyField(Country)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("car-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.company)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company} fresh-{self.isFresh} used for {self.used} years country-{self.country}"
