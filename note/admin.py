from django.contrib import admin

# Register your models here.
from note.models import *

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
