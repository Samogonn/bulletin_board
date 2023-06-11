from django.contrib import admin
from .models import Announcement, Category, Response

admin.site.register(Announcement)
admin.site.register(Category)
admin.site.register(Response)
