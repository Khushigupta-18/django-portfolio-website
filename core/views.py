from django.shortcuts import render
from portfolio.models import Project, Skill, Service
from contact.models import ContactMessage


def home(request):
    projects = Project.objects.filter().order_by('order')[:6]
    skills = Skill.objects.filter().order_by('order')
    services = Service.objects.filter().order_by('order')
    message_count = ContactMessage.objects.count()
    
    context = {
        'projects': projects,
        'skills': skills,
        'services': services,
        'message_count': message_count,
    }
    return render(request, 'core/home.html', context)
