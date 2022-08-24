from django.contrib import admin
from .models import Match
from .forms import MatchForm

class MatchAdmin(admin.ModelAdmin):
   list_display = ['bname', 'gname']
   form = MatchForm

admin.site.register(Match, MatchAdmin)
