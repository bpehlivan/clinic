# Generated by Django 5.1.1 on 2024-09-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='license_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
