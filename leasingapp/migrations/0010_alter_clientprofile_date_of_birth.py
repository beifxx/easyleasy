# Generated by Django 4.1.2 on 2022-10-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingapp', '0009_alter_clientprofile_apartment_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]