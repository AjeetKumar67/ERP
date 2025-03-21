# from django.contrib import admin
# from .models import ClassSection, Section, Subject

# @admin.register(ClassSection)
# class ClassAdmin(admin.ModelAdmin):
#     list_display = ('name', 'grade', 'created_at')
#     search_fields = ('name',)

# @admin.register(Section)
# class SectionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'class_assigned', 'created_at')
#     search_fields = ('name',)

# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'class_assigned')
#     search_fields = ('name', 'code')