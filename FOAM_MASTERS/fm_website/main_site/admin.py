from django.contrib import admin
from .models import *

admin.site.site_header = 'Foam Masters administration'

admin.site.register(Subscriber)
admin.site.register(SentMail)
admin.site.register(RecievedMail)
