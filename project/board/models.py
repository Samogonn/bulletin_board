from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Announcement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    title_tag = models.CharField("Тэг заголовка", max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField("Текст")
    publication_datetime = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse("announcement_details", kwargs={"pk": self.pk})
