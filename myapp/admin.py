from django.contrib import admin
# Register your models here.
from models import Person,Question,Education

admin.site.register(Person)
admin.site.register(Education)
#admin.site.register(SubCategory)
admin.site.register(Question)