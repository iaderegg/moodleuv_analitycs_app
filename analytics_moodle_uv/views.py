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

  courses_by_headquarter_queryset = DCourse.objects.filter(enddate__gte=init_year).values('headquarterid').annotate(total=Count('headquarterid')).order_by('-total')

  headquarters = []
  total_courses_headquarters = []

  

  for element in courses_by_headquarter_queryset:
    headquarters.append( element['headquarterid'] )   
    total_courses_headquarters.append( element['total'] )

  courses_by_headquarter_dict = {'headquarters': headquarters, 'total': total_courses_headquarters}

  courses_by_headquarter_json = json.dumps( courses_by_headquarter_dict )
  
  #courses_by_headquarter_json = serializers.serialize('json', courses_by_headquarter, fields=('headquarterid','total'))

  # Indicadores Usuarios Campus Virtual
  total_users_uv = DUser.objects.count()
  #total_users_current_semester_uv = DUser.objects.filter(timecreated_gte=init_current_semester).count()

  data = {
    'is_valid': False,
    'total_courses_uv': total_courses_uv,
    'total_courses_current_year_uv': total_courses_current_year,
    'total_regular_courses': total_regular_courses,
    'total_no_regular_courses': total_no_regular_courses,
    'courses_by_headquarter': courses_by_headquarter_json,
    'total_users_uv': total_users_uv,
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

