# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-18 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_books_app', '0003_book_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='book',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='user_books_app.User'),
        ),
    ]
