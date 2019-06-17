from django.contrib import admin
from martor.widgets import AdminMartorWidget
from main.models import Main, Category, Entry

# Register your models here.

admin.site.register(Main)
admin.site.register(Category)
admin.site.register(Entry)
