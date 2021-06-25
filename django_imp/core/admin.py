from django.contrib import admin
from .models import Software, Categoria, RequisitosMin

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Software)
admin.site.register(RequisitosMin)