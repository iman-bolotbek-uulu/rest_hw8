# Generated by Django 4.1.5 on 2023-01-10 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='statustweet',
            unique_together=set(),
        ),
    ]
