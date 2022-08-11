# Generated by Django 4.1 on 2022-08-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recordsheet', '0008_delete_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.IntegerField()),
                ('exam', models.IntegerField()),
                ('grade', models.CharField(max_length=2)),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordsheet.students')),
            ],
        ),
    ]