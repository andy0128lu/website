from django.contrib import admin
from .models import Subject, Comment

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'date', 'content')
    list_filter = ('date',)
    ordering = ('-date',)
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'content')
    list_filter = ('date',)
    ordering = ('-date',)

#admin.site.register(Subject)
#admin.site.register(Comment)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Comment, CommentAdmin)

 
