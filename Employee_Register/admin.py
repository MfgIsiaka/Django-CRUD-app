from django.contrib import admin
from .models import Position, Employee

# Registering the Position model
admin.site.register(Position)

# Registering the Manager model
admin.site.register(Employee)
