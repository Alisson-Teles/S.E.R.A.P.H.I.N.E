from django.contrib import admin

# Register your models here.
from .models import Chat, Topic, Message

admin.site.register(Chat) 
admin.site.register(Topic)
admin.site.register(Message)