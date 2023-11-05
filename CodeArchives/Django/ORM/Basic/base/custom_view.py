from django.http import HttpResponse
from .models import Classroom
from django.db import connection

def get_only_fields(request):
    # only_names = Classroom.objects.filter(id=1).values_list('name')
    raw_query = Classroom.objects.raw("select id,name from base_classroom where gender='M'")
    for item in raw_query:
        print(item.mark)

    # another way to execute raw queries like mysql-connector

    cursor = connection.cursor()
    cursor.execute('select id, name from base_classroom')
    all_values = cursor.fetchall()
    print(all_values)    
    print(connection.queries)

    return HttpResponse('')