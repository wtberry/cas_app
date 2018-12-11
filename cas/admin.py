from django.contrib import admin
from .models import Post, Client, Tutor, Professor, Session, Course, Supervisor
# Register your models here.

admin.site.register(Post)
admin.site.register(Client)
admin.site.register(Tutor)
admin.site.register(Professor)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Supervisor)

