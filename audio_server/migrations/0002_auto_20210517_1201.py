# Generated by Django 3.2.2 on 2021-05-17 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio_server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiobook',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='podcast',
            old_name='ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='ID',
            new_name='id',
        ),
    ]