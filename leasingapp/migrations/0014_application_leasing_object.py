# Generated by Django 4.1.2 on 2022-10-25 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingapp', '0013_alter_application_client_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='leasing_object',
            field=models.CharField(max_length=255, null=True),
        ),
    ]