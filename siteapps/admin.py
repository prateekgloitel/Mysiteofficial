from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Intrest)
admin.site.register(Certificate)