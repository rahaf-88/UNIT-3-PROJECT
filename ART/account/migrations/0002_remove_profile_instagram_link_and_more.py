# Generated by Django 5.0.3 on 2024-04-04 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linked_link',
        ),
    ]