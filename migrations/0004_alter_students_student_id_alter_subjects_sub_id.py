# Generated by Django 4.1 on 2022-08-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordsheet', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='sub_id',
            field=models.IntegerField(),
        ),
    ]
