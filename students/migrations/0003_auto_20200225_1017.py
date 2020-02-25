# Generated by Django 3.0.3 on 2020-02-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0007_auto_20200217_2152'),
        ('students', '0002_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='departments.SelectedCourse', verbose_name='courses'),
        ),
    ]
