# Generated by Django 5.0.3 on 2024-11-17 17:53

import django.db.models.deletion
from django.db import migrations, models


def set_default_profile(apps, schema_editor):
    IndividualRecordForm = apps.get_model("api", "IndividualRecordForm")
    Profile = apps.get_model("api", "Profile")
    for form in IndividualRecordForm.objects.all():
        try:
            # Assign a valid Profile based on your business logic
            form.profile = Profile.objects.first()  # Replace with a valid query
            form.save()
        except Profile.DoesNotExist:
            form.profile = None
            form.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_delete_user_remove_resource_author_resource_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualrecordform',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.profile'),
        ),
    ]
