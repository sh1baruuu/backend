# Generated by Django 5.0.3 on 2024-10-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_reommendation_routineinterview_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualRecordForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.TextField(max_length=255)),
                ('firstname', models.TextField(max_length=255)),
                ('middlename', models.TextField(max_length=255)),
                ('year', models.TextField()),
                ('section', models.TextField()),
                ('completeAddress', models.TextField(max_length=255)),
                ('fatherName', models.TextField()),
                ('fatherOccupation', models.TextField()),
                ('fatherContactNumber', models.TextField()),
                ('fatherEmailAddress', models.TextField()),
                ('motherName', models.TextField()),
                ('motherOccupation', models.TextField()),
                ('motherContactNumber', models.TextField()),
                ('motherEmailAddress', models.TextField()),
                ('parents', models.JSONField(default=list)),
                ('living_with', models.JSONField(default=list)),
                ('relationship', models.TextField()),
                ('club', models.TextField()),
            ],
        ),
    ]
