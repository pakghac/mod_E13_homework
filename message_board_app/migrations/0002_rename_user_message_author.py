# Generated by Django 4.2.4 on 2023-08-06 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_board_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='author',
        ),
    ]
