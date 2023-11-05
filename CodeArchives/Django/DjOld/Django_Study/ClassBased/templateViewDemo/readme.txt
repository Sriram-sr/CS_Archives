For using templates view in views 
from django.views.generic.base import TemplatesView
create a default function def get_context_data(self) inside a class you inheriting base TemplatesView class
and call in url with your class.as_view() method

or you can call staticcally in urls file by importing

from django.views.generic import TemplatesView
addding two extra arguments in urls