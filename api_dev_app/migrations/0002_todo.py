# Generated by Django 3.2 on 2021-04-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_dev_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'todo',
            },
        ),
    ]
