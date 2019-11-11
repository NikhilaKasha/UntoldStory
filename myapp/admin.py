from django.contrib import admin


from .models import Profile, Interest, Story, Saved, ReadLater

class ProfileList(admin.ModelAdmin):
    list_display = ('Profile_name','role', 'phone_number', 'email', 'created_date', 'updated_date')
    list_filter = ('Profile_name', 'role')
    search_fields = ('Profile_name', 'role')
    ordering = ['Profile_name']

class InterestList(admin.ModelAdmin):
    list_display = ( 'Profile_name', 'Interest_category')
    list_filter = ( 'Profile_name','Interest_category' )
    search_fields = ('Profile_name', 'Interest_category')
    ordering = ['Profile_name']

class StoryList(admin.ModelAdmin):
    list_display = ('Profile_name', 'title', 'p_description', 'created_date','updated_date')
    list_filter = ('Profile_name', 'title')
    search_fields = ('Profile_name', 'title')
    ordering = ['Profile_name']


admin.site.register(Profile, ProfileList)
admin.site.register(Interest, InterestList)
admin.site.register(Story, StoryList)
admin.site.register(Saved)
admin.site.register(ReadLater)

