# Generated by Django 3.0.6 on 2020-05-18 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200518_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='deleted',
        ),
    ]