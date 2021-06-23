from django.contrib import admin
from .models import Software, Categoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Software)