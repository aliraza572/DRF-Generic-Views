# Generated by Django 3.1.5 on 2021-01-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
