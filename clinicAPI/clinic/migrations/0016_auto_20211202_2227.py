# Generated by Django 3.0.8 on 2021-12-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0015_auto_20211202_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='content',
            field=models.CharField(max_length=3000),
        ),
    ]