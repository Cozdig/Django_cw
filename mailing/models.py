from django.db import models
from django.utils import timezone


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

class Mailings(models.Model):

    CREATED = 'Создана'
    STARTED = 'Запущена'
    FINISHED = 'Завершена'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (FINISHED, 'Завершена'),
    ]

    start_time = models.DateTimeField(null=False, blank=False, verbose_name="Дата и время начала отправки")
    end_time = models.DateTimeField(null=False, blank=False, verbose_name="Дата и время окончания отправки")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="mailings", verbose_name="Сообщение")
    recipients = models.ManyToManyField(Recipient, related_name="mailings", verbose_name="Получатели")

    def __str__(self):
        return f"Дата: {self.start_time} Получатель:{self.recipients}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        ordering = ['start_time', ]

    def update_status(self, save=True):
        now = timezone.now()

        if now < self.start_time:
            new_status = self.CREATED
        elif self.start_time <= now <= self.end_time:
            new_status = self.STARTED
        else:
            new_status = self.FINISHED

        if self.status != new_status:
            self.status = new_status
            if save:
                self.save(update_fields=['status'])

        return new_status
