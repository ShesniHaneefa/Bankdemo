# Generated by Django 4.1.1 on 2023-01-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_delete_inputform'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('adrress', models.CharField(max_length=250)),
            ],
        ),
    ]
