from django import forms
from django_filters import FilterSet, DateFilter
from .models import Post
import django_filters


class NewFilter(FilterSet):
    date_in = DateFilter (field_name ='date_in', widget=forms.DateInput(attrs={'type':'date'}), label='Дата', lookup_expr='date__gte')
    
    class Meta:
        model = Post
        fields = {'title':['icontains'], 'author': ['exact'],}