# Generated by Django 5.1.4 on 2024-12-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_alter_topic_category_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Science', 'Science'), ('Mathematics', 'Mathematics'), ('Technology', 'Technology'), ('Engineering', 'Engineering')], max_length=50),
        ),
    ]
