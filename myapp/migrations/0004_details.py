# Generated by Django 4.2.1 on 2023-06-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_blog_body_alter_blog_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=25)),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
    ]
