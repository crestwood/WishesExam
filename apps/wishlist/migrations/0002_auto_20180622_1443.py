# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-22 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField(max_length=1000)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='secret',
            name='liked_users',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='uploader',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.DeleteModel(
            name='Secret',
        ),
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creates', to='wishlist.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='wishlist.User'),
        ),
    ]