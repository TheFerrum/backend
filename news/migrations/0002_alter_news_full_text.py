# Generated by Django 4.2 on 2023-05-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='full_text',
            field=models.TextField(verbose_name='News_Article'),
        ),
    ]
