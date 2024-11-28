from django.db import models

# Create your models here.


class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    photo = models.ImageField(upload_to='lawyers/photos/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
