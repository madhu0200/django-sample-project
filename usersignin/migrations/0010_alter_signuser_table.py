# Generated by Django 4.0.4 on 2022-04-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersignin', '0009_alter_signuser_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='signuser',
            table='usersignin_register',
        ),
    ]
