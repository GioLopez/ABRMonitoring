# Generated by Django 3.1 on 2020-08-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlsmanifestparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hlsmanifestparser',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]