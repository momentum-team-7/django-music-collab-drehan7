# Generated by Django 3.1.7 on 2021-03-02 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210301_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='song_year',
            new_name='album_year',
        ),
    ]