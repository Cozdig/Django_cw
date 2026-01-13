from django.db import models


# Create your models here.

class Recipient(models.Model):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=200, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'
        ordering = ['fullname', ]


class Message(models.Model):
    topic = models.CharField(max_length=200, verbose_name="Тема")
    content = models.TextField(verbose_name="Содержимое")

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ['topic', ]
