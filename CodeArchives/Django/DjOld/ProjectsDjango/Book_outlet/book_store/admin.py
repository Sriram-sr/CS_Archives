from django.contrib import admin
from book_store.models import Book,Author,Address,Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("title",)  # this is to make the model fields read only and not edit
    pass


admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)