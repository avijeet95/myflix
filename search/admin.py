from django.contrib import admin

# Register your models here.
from .models import Search
from .forms import SearchForm

admin.site.register(Search)

class SearchAdmin(admin.ModelAdmin):
	list_display=["__unicode__",'name']
	form = SearchForm