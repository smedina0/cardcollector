# Generated by Django 4.1.7 on 2023-04-08 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('tool', models.CharField(choices=[('C', 'Cotton Swab'), ('B', 'Brush'), ('S', 'Sponge'), ('P', 'Paper Towel'), ('A', 'Air Duster'), ('O', 'Other')], default='C', max_length=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.card')),
            ],
        ),
    ]
