# Generated by Django 3.0.6 on 2020-05-18 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200517_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='deleted',
            new_name='approved',
        ),
    ]
