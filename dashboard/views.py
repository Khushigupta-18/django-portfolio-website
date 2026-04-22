from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from portfolio.models import Project, Skill, Service
from contact.models import ContactMessage


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'dashboard/login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required
def dashboard(request):
    project_count = Project.objects.count()
    skill_count = Skill.objects.count()
    message_count = ContactMessage.objects.count()
    service_count = Service.objects.count()
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    
    context = {
        'project_count': project_count,
        'skill_count': skill_count,
        'message_count': message_count,
        'service_count': service_count,
        'recent_messages': recent_messages,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def message_list(request):
    messages_list = ContactMessage.objects.order_by('-created_at')
    return render(request, 'dashboard/messages.html', {'messages': messages_list})


@login_required
def message_delete(request, pk):
    message = ContactMessage.objects.get(pk=pk)
    message.delete()
    messages.success(request, 'Message deleted successfully!')
    return redirect('dashboard_messages')
