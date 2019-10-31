# Generated by Django 2.2.6 on 2019-10-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('post', models.ManyToManyField(blank=True, related_name='tags', to='tag.Post')),
            ],
        ),
    ]
