# Generated by Django 3.2.3 on 2021-06-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='allstudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Mail_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
