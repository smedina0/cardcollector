# Generated by Django 4.1.7 on 2023-04-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_vendor_alter_cleaning_options_alter_cleaning_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='vendors',
            field=models.ManyToManyField(to='main_app.vendor'),
        ),
    ]
