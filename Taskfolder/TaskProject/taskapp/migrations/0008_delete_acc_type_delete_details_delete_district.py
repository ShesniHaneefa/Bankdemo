# Generated by Django 4.1.1 on 2023-01-30 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0007_acc_type_district_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acc_type',
        ),
        migrations.DeleteModel(
            name='Details',
        ),
        migrations.DeleteModel(
            name='District',
        ),
    ]
