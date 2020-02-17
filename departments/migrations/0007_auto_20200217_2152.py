# Generated by Django 3.0.3 on 2020-02-17 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0006_departmentperiod_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='selected_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.SelectedCourse', verbose_name='course'),
        ),
    ]