# Generated by Django 4.2.8 on 2024-03-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversationhandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='rate',
            field=models.FloatField(default=0, max_length=5),
        ),
    ]
