from django.contrib import admin

# Register your models here.
from .models import Mailing, Takingone, Wordsofmail

admin.site.register(Mailing)
admin.site.register(Takingone)
admin.site.register(Wordsofmail)