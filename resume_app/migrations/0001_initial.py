# Generated by Django 3.2.6 on 2021-08-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernamename', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('phonenumber', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
    ]