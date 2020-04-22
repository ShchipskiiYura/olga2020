from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['nameTask', 'priority', 'startDate', 'hoursNumber', 'completionStatus', 'nameTask', 'priority',
                    'startDate', 'hoursNumber', 'completionStatus']


@admin.register(Employee)
class EmpoyeeAdmin(admin.ModelAdmin):
    list_display = ['fullName', 'birthDate', 'telephoneNumber', 'workExperience', 'position', 'employmentDate']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'alternativeLevel', 'scope', 'budget', 'duration']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'capitalization', 'focus', 'foundationDate', 'rating']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'teamLead', 'projectManager', 'costPerHour', 'programers', 'technologyStack',
                    'participantsNumber', 'fullName', 'salary', 'employmentStatus', 'direction', 'position']


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['address', 'purchaseDate', 'employees', 'schedule', 'area', 'jobsNumber', 'priceRent']
