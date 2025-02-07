from django.contrib import admin
from rango.models import Category, Page

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Page)
admin.site.register(Category, CategoryAdmin) # Update the registration to include this customised interface
