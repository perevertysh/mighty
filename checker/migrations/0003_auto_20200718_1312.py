# Generated by Django 2.2.10 on 2020-07-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0002_answer_check_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='создано'),
        ),
    ]
