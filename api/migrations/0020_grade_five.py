# Generated by Django 5.0.3 on 2024-10-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_grade_four_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade_Five',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('sex', models.JSONField(default=list)),
                ('gradeLevel', models.CharField(max_length=255)),
                ('section', models.JSONField(default=list)),
                ('raw_score', models.CharField(max_length=255)),
                ('percentile', models.CharField(max_length=255)),
                ('stanine', models.CharField(max_length=255)),
                ('verbal_interpretation', models.JSONField(default=list)),
            ],
        ),
    ]
