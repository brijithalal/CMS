# Generated by Django 5.1.4 on 2025-01-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_alter_patient_insurance_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='clinic/images/'),
        ),
    ]
