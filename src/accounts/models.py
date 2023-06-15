from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    bio = models.TextField(default="Немного о себе ...")
    user_photo = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def __str__(self):
        return f"{self.user}"
