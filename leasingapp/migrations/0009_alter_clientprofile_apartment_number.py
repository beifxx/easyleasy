# Generated by Django 4.1.2 on 2022-10-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingapp', '0008_alter_clientprofile_house_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='apartment_number',
            field=models.CharField(max_length=50),
        ),
    ]
