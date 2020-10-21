from django.contrib import admin
from .models import Question


# we need to tell admin that Question objects have admin interface

admin.site.register(Question)