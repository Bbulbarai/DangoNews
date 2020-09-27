from django.contrib import admin

from .models import News, Superuser, User_model, Login, Event

admin.site.register(News)
admin.site.register(Superuser)
admin.site.register(User_model)
admin.site.register(Login)
admin.site.register(Event)