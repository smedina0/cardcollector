# Generated by Django 4.1.7 on 2023-04-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cleaning',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(verbose_name='cleaning date'),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='tool',
            field=models.CharField(choices=[('C', 'Cotton Swab'), ('B', 'Brush'), ('S', 'Sponge'), ('P', 'Paper Towel'), ('A', 'Air Duster'), ('O', 'Other')], default='C', max_length=1, verbose_name='cleaning tool'),
        ),
    ]
