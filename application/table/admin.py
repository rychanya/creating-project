from django.contrib import admin

from table.models import CSVPath, Columns
# Register your models here.

admin.site.register(Columns)
admin.site.register(CSVPath)

