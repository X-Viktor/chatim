from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название чата')
    members = models.ManyToManyField(
        User,
        related_name='chats',
        verbose_name='Участники'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    message = models.CharField(max_length=120, verbose_name='Сообщение')
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Отправитель'
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Чат'
    )
    date_sending = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата отправки'
    )

    def __str__(self):
        return self.sender.username

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['date_sending']
