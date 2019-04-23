from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

from analytics_moodle_uv.models import *

import datetime
import time

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
def get_general_summary(request):

  init_current_semester = get_init_current_semester()

  # Indicadores Cursos Campus Virtual
  total_courses_uv = DCourse.objects.count()
  total_courses_current_semester_uv = DCourse.objects.filter(timecreated__gte=init_current_semester).count()

  # Indicadores Usuarios Campus Virtual
  total_users_uv = DUser.objects.count()
  #total_users_current_semester_uv = DUser.objects.filter(timecreated_gte=init_current_semester).count()

  data = {
    'is_valid': False,
    'total_courses_uv': total_courses_uv,
    'total_courses_current_semester_uv': total_courses_current_semester_uv,
    'total_users_uv': total_users_uv,
  }

  if request.is_ajax():

    data.update(is_valid=True)

  return JsonResponse(data)

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


