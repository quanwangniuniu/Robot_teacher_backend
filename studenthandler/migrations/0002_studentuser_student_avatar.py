# Generated by Django 4.2.8 on 2024-03-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenthandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='student_avatar',
            field=models.CharField(default='https://api.dicebear.com/7.x/miniavs/svg?seed=1', max_length=200),
        ),
    ]