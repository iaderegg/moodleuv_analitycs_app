# Generated by Django 3.2 on 2021-04-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_moodle_uv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DAcademicPeriods',
            fields=[
                ('technical_surrogate_key_field', models.BigAutoField(db_column='technical/surrogate key field', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('timestart', models.BigIntegerField(blank=True, null=True)),
                ('timecompletion', models.BigIntegerField(blank=True, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'd_academic_periods',
                'managed': False,
            },
        ),
    ]
