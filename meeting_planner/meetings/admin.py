from django.contrib import admin

# Register your models here.

# Start by importing our meeting class
from .models import Meeting

admin.site.register(Meeting)
