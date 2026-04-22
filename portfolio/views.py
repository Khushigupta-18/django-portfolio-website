from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, Skill, Service


def project_list(request):
    projects = Project.objects.all().order_by('order')
    return render(request, 'dashboard/projects.html', {'projects': projects})


def project_add(request):
    if request.method == 'POST':
        project = Project(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            tech_stack=request.POST.get('tech_stack'),
            github_link=request.POST.get('github_link'),
            live_link=request.POST.get('live_link'),
            order=request.POST.get('order', 0)
        )
        project.save()
        messages.success(request, 'Project added successfully!')
        return redirect('dashboard_projects')
    return render(request, 'dashboard/project_form.html', {'project': None})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.tech_stack = request.POST.get('tech_stack')
        project.github_link = request.POST.get('github_link')
        project.live_link = request.POST.get('live_link')
        project.order = request.POST.get('order', 0)
        if request.FILES.get('image'):
            project.image = request.FILES.get('image')
        project.save()
        messages.success(request, 'Project updated successfully!')
        return redirect('dashboard_projects')
    return render(request, 'dashboard/project_form.html', {'project': project})


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('dashboard_projects')


def skill_list(request):
    skills = Skill.objects.all().order_by('category', 'order')
    return render(request, 'dashboard/skills.html', {'skills': skills})


def skill_add(request):
    if request.method == 'POST':
        skill = Skill(
            name=request.POST.get('name'),
            percentage=request.POST.get('percentage'),
            category=request.POST.get('category'),
            order=request.POST.get('order', 0)
        )
        skill.save()
        messages.success(request, 'Skill added successfully!')
        return redirect('dashboard_skills')
    return render(request, 'dashboard/skill_form.html', {'skill': None})


def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.name = request.POST.get('name')
        skill.percentage = request.POST.get('percentage')
        skill.category = request.POST.get('category')
        skill.order = request.POST.get('order', 0)
        skill.save()
        messages.success(request, 'Skill updated successfully!')
        return redirect('dashboard_skills')
    return render(request, 'dashboard/skill_form.html', {'skill': skill})


def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('dashboard_skills')


def service_list(request):
    services = Service.objects.all().order_by('order')
    return render(request, 'dashboard/services.html', {'services': services})


def service_add(request):
    if request.method == 'POST':
        service = Service(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            icon=request.POST.get('icon'),
            order=request.POST.get('order', 0)
        )
        service.save()
        messages.success(request, 'Service added successfully!')
        return redirect('dashboard_services')
    return render(request, 'dashboard/service_form.html', {'service': None})


def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.title = request.POST.get('title')
        service.description = request.POST.get('description')
        service.icon = request.POST.get('icon')
        service.order = request.POST.get('order', 0)
        service.save()
        messages.success(request, 'Service updated successfully!')
        return redirect('dashboard_services')
    return render(request, 'dashboard/service_form.html', {'service': service})


def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect('dashboard_services')
