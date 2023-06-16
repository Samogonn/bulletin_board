from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField("Название", max_length=255)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("board")


class Announcement(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    title_tag = models.CharField("Тэг заголовка", max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    publication_datetime = models.DateTimeField("Дата публикации", auto_now_add=True)
    text = RichTextField("Текст", blank=True, null=True)
    image = models.ImageField("Картинка", null=True, blank=True, upload_to="images/")
    category = models.ManyToManyField(Category, verbose_name="Категория")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("announcement_details", kwargs={"pk": self.pk})


class Response(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        related_name="responses",
        on_delete=models.CASCADE,
        verbose_name="Объявление",
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField(default="")
    datetime_added = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField("Отклик принят?", default=False)

    def __str__(self):
        return f"{self.announcement.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("board")
