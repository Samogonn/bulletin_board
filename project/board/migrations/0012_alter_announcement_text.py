# Generated by Django 4.2.2 on 2023-06-09 09:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_remove_response_body_response_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
