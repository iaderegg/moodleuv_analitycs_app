# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class DCourse(models.Model):
    technical_surrogate_key_field = models.BigAutoField(db_column='technical/surrogate key field', unique=True, primary_key=True)  # Field renamed to remove unsuitable characters.
    id_moodle = models.IntegerField(blank=True, null=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=21, blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_course'


class DCourseCategories(models.Model):
    id_dwh = models.BigIntegerField(primary_key=True)
    id_moodle = models.BigIntegerField()
    id_category_parent = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_course_categories'


class DDate(models.Model):
    date_dim_id = models.IntegerField(primary_key=True)
    date_actual = models.DateField()
    epoch = models.BigIntegerField()
    day_suffix = models.CharField(max_length=4)
    day_name = models.CharField(max_length=9)
    day_of_week = models.IntegerField()
    day_of_month = models.IntegerField()
    day_of_quarter = models.IntegerField()
    day_of_year = models.IntegerField()
    week_of_month = models.IntegerField()
    week_of_year = models.IntegerField()
    week_of_year_iso = models.CharField(max_length=10)
    month_actual = models.IntegerField()
    month_name = models.CharField(max_length=9)
    month_name_abbreviated = models.CharField(max_length=3)
    quarter_actual = models.IntegerField()
    quarter_name = models.CharField(max_length=9)
    year_actual = models.IntegerField()
    first_day_of_week = models.DateField()
    last_day_of_week = models.DateField()
    first_day_of_month = models.DateField()
    last_day_of_month = models.DateField()
    first_day_of_quarter = models.DateField()
    last_day_of_quarter = models.DateField()
    first_day_of_year = models.DateField()
    last_day_of_year = models.DateField()
    mmyyyy = models.CharField(max_length=6)
    mmddyyyy = models.CharField(max_length=10)
    weekend_indr = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'd_date'


class DFaculty(models.Model):
    technical_surrogate_key_field = models.BigAutoField(db_column='technical/surrogate key field', unique=True, primary_key=True)  # Field renamed to remove unsuitable characters.
    id_moodle = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    category_parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_faculty'


class DHeadquarter(models.Model):
    technical_surrogate_key_field = models.BigAutoField(db_column='technical/surrogate key field', unique=True, primary_key=True)  # Field renamed to remove unsuitable characters.
    id_univalle = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_headquarter'


class DUser(models.Model):
    technical_surrogate_key_field = models.BigAutoField(db_column='technical/surrogate key field', unique=True, primary_key=True)  # Field renamed to remove unsuitable characters.
    id_moodle = models.IntegerField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_user'

class DAcademicPeriods(models.Model):
    technical_surrogate_key_field = models.BigAutoField(db_column='technical/surrogate key field', unique=True, primary_key=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    timestart = models.BigIntegerField(blank=True, null=True)
    timecompletion = models.BigIntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'd_academic_periods'

class FCourseCreation(models.Model):
    contextlevel = models.BigIntegerField(blank=True, null=True)
    contextid = models.BigIntegerField(blank=True, null=True)
    date_dim_id = models.IntegerField(blank=True, null=True)
    id_course_dwh = models.BigIntegerField(blank=True, null=True)
    id_dwh = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_course_creation'

def __str__(self):
    return self.field_name
