# Generated by Django 4.1.2 on 2022-10-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingapp', '0011_alter_clientprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
