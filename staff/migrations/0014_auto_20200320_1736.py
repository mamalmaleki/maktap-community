# Generated by Django 3.0.3 on 2020-03-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_auto_20200320_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='version',
            field=models.IntegerField(blank=True, default=0, verbose_name='current version'),
        ),
        migrations.AlterField(
            model_name='student',
            name='version',
            field=models.IntegerField(blank=True, default=0, verbose_name='current version'),
        ),
    ]