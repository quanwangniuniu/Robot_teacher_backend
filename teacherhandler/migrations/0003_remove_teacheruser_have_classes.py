# Generated by Django 4.2.8 on 2024-03-03 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherhandler', '0002_alter_teacheruser_have_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacheruser',
            name='have_classes',
        ),
    ]