# Generated by Django 3.2.3 on 2021-06-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0015_zoommeet'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enter_course_title', models.CharField(max_length=100)),
                ('from_url', models.CharField(max_length=100)),
                ('fileToUpload', models.ImageField(upload_to='')),
                ('overview_URL', models.CharField(max_length=100)),
                ('Enter_requirements', models.CharField(max_length=100)),
                ('Enter_outcome', models.CharField(max_length=100)),
                ('Enter_tags', models.CharField(max_length=100)),
                ('Amount', models.CharField(max_length=100)),
                ('Enter_meta_title', models.CharField(max_length=100)),
                ('Short_description', models.TextField()),
                ('Meta_description', models.TextField()),
                ('Course_level', models.CharField(max_length=100)),
                ('Provider', models.CharField(max_length=100)),
                ('Free_course', models.CharField(max_length=100)),
                ('Discount', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
    ]
