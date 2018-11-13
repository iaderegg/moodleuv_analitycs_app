from django.shortcuts import render

def general_summary(request):

  context = {
    'testing': 'testing'
  }

  return render(request, 'analytics_moodle_uv/general_summary.html', context)
