from django.shortcuts import render
from django.views.generic import TemplateView
import sys
# Create your views here.
print(sys.path)
def func(request):
    return render(request, 'second_task/func_template.html')

class Class2(TemplateView):
    template_name = 'second_task/class_template.html'