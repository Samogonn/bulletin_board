# Generated by Django 4.2.2 on 2023-06-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_alter_announcement_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='snippet',
            field=models.CharField(default='Начьните писать объявление...', max_length=255),
        ),
    ]