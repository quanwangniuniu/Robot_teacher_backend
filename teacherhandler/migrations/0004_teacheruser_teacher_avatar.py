# Generated by Django 4.2.8 on 2024-03-14 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherhandler', '0003_remove_teacheruser_have_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacheruser',
            name='teacher_avatar',
            field=models.CharField(default='https://api.dicebear.com/7.x/miniavs/svg?seed=1', max_length=200),
        ),
    ]
