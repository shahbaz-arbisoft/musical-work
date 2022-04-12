from django.contrib import admin

# Register your models here.
from musicalapp.models import Work, Contributor

admin.site.register(Work)
admin.site.register(Contributor)