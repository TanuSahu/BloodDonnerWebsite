# Generated by Django 4.1 on 2022-09-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bldapp', '0002_alter_userprofile_bloodgroup_alter_userprofile_dob_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddonertransactions',
            name='donationdatetime',
        ),
        migrations.AddField(
            model_name='blooddonertransactions',
            name='donationdate',
            field=models.DateField(db_column='Donation Date', null=True),
        ),
        migrations.AddField(
            model_name='blooddonertransactions',
            name='donationtime',
            field=models.TimeField(db_column='Donation Time', null=True),
        ),
    ]