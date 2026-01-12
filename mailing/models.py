from django.db import models


# Create your models here.

class Recipient(models.Model):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=200, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return self.email