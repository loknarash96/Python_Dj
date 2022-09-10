from django.contrib import admin
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',) #кортеж
    list_filter = ('is_published','time_create')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',) #Кортеж, поэтому и запятая


admin.site.register(Women, WomenAdmin,) #появилось на админ панели, вторым параметром второстепенные классы
admin.site.register(Category,CategoryAdmin)