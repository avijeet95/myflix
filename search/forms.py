from .models import Search
from django.forms import ModelForm

class SearchForm(ModelForm):
	class Meta:
		model = Search
		fields = ['name','year']

	