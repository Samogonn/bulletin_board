# Generated by Django 4.2.2 on 2023-06-07 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_announcement_date_alter_announcement_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='date',
            new_name='datetime',
        ),
    ]
