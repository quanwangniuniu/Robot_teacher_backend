# Generated by Django 4.2.8 on 2024-02-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('conversation_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('user_type', models.CharField(default='student', max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=1)),
                ('robot_model', models.CharField(default='qwen-max', max_length=100)),
                ('robot_prompt', models.CharField(default='programing teacher', max_length=300)),
                ('roles', models.CharField(default='programing teacher', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('conversation_id', models.IntegerField()),
                ('message_content', models.CharField(max_length=2000)),
                ('message_type', models.CharField(max_length=20)),
            ],
        ),
    ]
