from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from django.core import serializers

from analytics_moodle_uv.models import *

import datetime
import time
import json

# Vista del resumen general
def general_summary(request):

  context = {

  }

  return render(request, 'analytics_moodle_uv/general_summary.html', context)


# Vista de la sección de usuarios
def users_section(request):

  context = {
    
  }

  return render(request, 'analytics_moodle_uv/users.html', context)


# Retorna los datos a graficar en el resumen general
@csrf_exempt
def get_general_summary( request ):

  init_year = request.POST['init_year']

  if( init_year == 0 ):
    #init_year = get_current_year_timestamp()
    init_year = 1451624400
 
  regular_category = 30000

  # Indicadores Cursos Campus Virtual
  total_courses_uv = DCourse.objects.count()
  total_courses_current_year = DCourse.objects.filter(enddate__gte=init_year).count()
  total_regular_courses = DCourse.objects.filter(category__gte=30000).count()
  total_no_regular_courses = DCourse.objects.filter(category__lte=30000).count()

  courses_by_headquarter_queryset = DCourse.objects.filter(enddate__gte=init_year).values('headquartername').annotate(total=Count('headquartername')).order_by('-total')
  courses_by_faculty_queryset = DCourse.objects.filter(enddate__gte=init_year).values('facultyname').annotate(total=Count('facultyname')).order_by('-total')

  headquarters_courses = []
  total_courses_headquarters = []

  for element in courses_by_headquarter_queryset:
    headquarters_courses.append( element['headquartername'] )   
    total_courses_headquarters.append( element['total'] )

  courses_by_headquarter_dict = {'headquarters': headquarters_courses, 'total': total_courses_headquarters}
  courses_by_headquarter_json = json.dumps( courses_by_headquarter_dict )

  faculties = []
  total_courses_faculties =[]

  for element in courses_by_faculty_queryset:
    faculties.append( element['facultyname'] )   
    total_courses_faculties.append( element['total'] )

  courses_by_faculties_dict = {'faculties': faculties, 'total': total_courses_faculties}
  courses_by_faculties_json = json.dumps( courses_by_faculties_dict ) 
    
  # Indicadores Usuarios Campus Virtual
  total_users = DUser.objects.count()
  total_students = DUser.objects.filter(isstudent = True).count()
  total_other_users = DUser.objects.filter(isstudent = False).count()

  users_by_headquarter_queryset = DCourse.objects.all().values('headquartername').annotate(total=Count('headquartername')).order_by('-total')
  
  headquarters_users = []
  total_users_headquarters = []

  for element in users_by_headquarter_queryset:
    headquarters_users.append( element['headquartername'] )   
    total_users_headquarters.append( element['total'] )

  users_by_headquarter_dict = {'headquarters': headquarters_users, 'total': total_users_headquarters}
  users_by_headquarter_json = json.dumps( users_by_headquarter_dict )

  users_by_faculties_queryset = DCourse.objects.all().values('facultyname').annotate(total=Count('facultyname')).order_by('-total')

  faculties_users = [] 
  total_users_faculties = []

  for element in users_by_faculties_queryset:
    faculties_users.append( element['facultyname'] )   
    total_users_faculties.append( element['total'] )

  users_by_faculties_dict = {'faculties': faculties_users, 'total': total_users_faculties}
  users_by_faculties_json = json.dumps( users_by_faculties_dict )

  data = {
    'is_valid': False,
    'total_courses_uv': total_courses_uv,
    'total_courses_current_year_uv': total_courses_current_year,
    'total_regular_courses': total_regular_courses,
    'total_no_regular_courses': total_no_regular_courses,
    'courses_by_headquarter': courses_by_headquarter_json,
    'courses_by_faculties': courses_by_faculties_json,
    'total_users': total_users,
    'total_students': total_students,
    'total_other_users': total_other_users,
    'users_by_headquarter': users_by_headquarter_json,
    'users_by_faculties': users_by_faculties_json
  }

  if request.is_ajax():

    data.update(is_valid=True)

  return JsonResponse(data)

def get_current_year_timestamp():

  today = datetime.datetime.now()
  year = today.year

  current_year = datetime.datetime(year, 1, 1, 0, 0, 0)

  return current_year

# Función que permite calcular el semestre actual
def get_init_current_semester():
    today = datetime.datetime.now()
    month = today.month

    if month <= 6:
        init_current_semester = datetime.datetime(today.year, 1, 1, 0, 0, 0)
    else:
        init_current_semester = datetime.datetime(today.year, 7, 1, 0, 0, 0)

    init_current_semester_timestamp = datetime.datetime.timestamp(init_current_semester)

    return init_current_semester_timestamp


# Función que retorna periodos académicos activos
def get_active_academic_periods():
    
    return 1

