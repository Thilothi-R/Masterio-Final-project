# Generated by Django 3.2.3 on 2021-06-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0019_auto_20210615_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=100)),
                ('Message', models.TextField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
