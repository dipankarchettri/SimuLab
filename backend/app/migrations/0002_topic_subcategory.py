# Generated by Django 5.1.4 on 2024-12-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='subcategory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
