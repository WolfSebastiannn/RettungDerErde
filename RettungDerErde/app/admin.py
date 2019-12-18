
from django.contrib import admin
from app.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    """Choice objects can be edited inline in the Poll editor."""
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
    """Definition of the Poll editor."""
    fieldsets = [
        (None, {'fields': ['text']}),
        (None, {'fields': ['Kurzbeschreibung']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['geplanter_Status']}),
        
    ]
    ##inlines = [ChoiceInline]
    list_display = ('text','Kurzbeschreibung', 'pub_date','geplanter_Status', )
    ##list_filter = ['pub_date']
    ##search_fields = ['text']   
    ##date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)

