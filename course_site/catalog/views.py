from django.shortcuts import render, get_object_or_404
from .models import Course

def home(request):
    return render(request, 'catalog/home.html')

def course_detail(request):
    if request.method == 'POST':
        course_code = request.POST.get('course_code', '').upper()
        course = get_object_or_404(Course, code=course_code)
        return render(request, 'catalog/detail.html', {'course': course})
    return render(request, 'catalog/home.html', {'error': 'Invalid course code'})