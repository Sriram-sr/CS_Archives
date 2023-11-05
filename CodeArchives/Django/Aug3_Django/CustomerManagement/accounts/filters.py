from distutils.command.build_scripts import first_line_re
from django_filters import FilterSet,DateFilter,CharFilter
from .models import *

class OrderFilter(FilterSet):
    start_date = DateFilter(field_name='date_created',lookup_expr='lte')
    end_date = DateFilter(field_name='date_created',lookup_expr='gte')
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('customer','date_created')
