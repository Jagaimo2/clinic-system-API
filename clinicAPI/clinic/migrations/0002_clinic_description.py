# Generated by Django 3.0.8 on 2021-11-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='description',
            field=models.CharField(max_length=800, null=True),
        ),
    ]