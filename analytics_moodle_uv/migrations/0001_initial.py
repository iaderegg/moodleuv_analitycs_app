# Generated by Django 2.1.3 on 2018-11-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_surrogate_key_field', models.BigIntegerField(db_column='technical/surrogate key field', unique=True)),
                ('id_moodle', models.IntegerField(blank=True, null=True)),
                ('fullname', models.CharField(blank=True, max_length=254, null=True)),
                ('category', models.IntegerField(blank=True, null=True)),
                ('format', models.CharField(blank=True, max_length=21, null=True)),
                ('shortname', models.CharField(blank=True, max_length=255, null=True)),
                ('timecreated', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_course',
            },
        ),
        migrations.CreateModel(
            name='DCourseCategories',
            fields=[
                ('id_dwh', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_moodle', models.BigIntegerField()),
                ('id_category_parent', models.BigIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_course_categories',
            },
        ),
        migrations.CreateModel(
            name='DDate',
            fields=[
                ('date_dim_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_actual', models.DateField()),
                ('epoch', models.BigIntegerField()),
                ('day_suffix', models.CharField(max_length=4)),
                ('day_name', models.CharField(max_length=9)),
                ('day_of_week', models.IntegerField()),
                ('day_of_month', models.IntegerField()),
                ('day_of_quarter', models.IntegerField()),
                ('day_of_year', models.IntegerField()),
                ('week_of_month', models.IntegerField()),
                ('week_of_year', models.IntegerField()),
                ('week_of_year_iso', models.CharField(max_length=10)),
                ('month_actual', models.IntegerField()),
                ('month_name', models.CharField(max_length=9)),
                ('month_name_abbreviated', models.CharField(max_length=3)),
                ('quarter_actual', models.IntegerField()),
                ('quarter_name', models.CharField(max_length=9)),
                ('year_actual', models.IntegerField()),
                ('first_day_of_week', models.DateField()),
                ('last_day_of_week', models.DateField()),
                ('first_day_of_month', models.DateField()),
                ('last_day_of_month', models.DateField()),
                ('first_day_of_quarter', models.DateField()),
                ('last_day_of_quarter', models.DateField()),
                ('first_day_of_year', models.DateField()),
                ('last_day_of_year', models.DateField()),
                ('mmyyyy', models.CharField(max_length=6)),
                ('mmddyyyy', models.CharField(max_length=10)),
                ('weekend_indr', models.BooleanField()),
            ],
            options={
                'managed': False,
                'db_table': 'd_date',
            },
        ),
        migrations.CreateModel(
            name='DFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_surrogate_key_field', models.BigIntegerField(db_column='technical/surrogate key field', unique=True)),
                ('id_moodle', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('category_parent', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_faculty',
            },
        ),
        migrations.CreateModel(
            name='DHeadquarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_surrogate_key_field', models.BigIntegerField(db_column='technical/surrogate key field', unique=True)),
                ('id_univalle', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_headquarter',
            },
        ),
        migrations.CreateModel(
            name='DUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_surrogate_key_field', models.BigIntegerField(db_column='technical/surrogate key field', unique=True)),
                ('id_moodle', models.IntegerField(blank=True, null=True)),
                ('fullname', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('timecreated', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_user',
            },
        ),
        migrations.CreateModel(
            name='FCourseCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contextlevel', models.BigIntegerField(blank=True, null=True)),
                ('contextid', models.BigIntegerField(blank=True, null=True)),
                ('date_dim_id', models.IntegerField(blank=True, null=True)),
                ('id_course_dwh', models.BigIntegerField(blank=True, null=True)),
                ('id_dwh', models.FloatField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'f_course_creation',
            },
        ),
    ]
