# Generated by Django 4.2.8 on 2024-03-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherhandler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacheruser',
            name='have_classes',
            field=models.CharField(max_length=500),
        ),
    ]