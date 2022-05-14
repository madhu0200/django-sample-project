# Generated by Django 4.0.4 on 2022-04-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersignin', '0002_registrateuser_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='registeruserss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobileno', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='registrateuser',
        ),
    ]
