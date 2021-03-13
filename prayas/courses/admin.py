from django.contrib import admin
from .models import Subject, Course, Module, Content, File, ContentType, Video, Text, Image


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    model = Content

# @admin.register(Module)
# class ContentAdmin(admin.ModelAdmin):
#     model = Module

@admin.register(ContentType)
class ContentAdmin(admin.ModelAdmin):
    model = ContentType

@admin.register(Video)
class ContentAdmin(admin.ModelAdmin):
    model = Video

@admin.register(Image)
class ContentAdmin(admin.ModelAdmin):
    model = Image

@admin.register(File)
class ContentAdmin(admin.ModelAdmin):
    model = File

@admin.register(Text)
class ContentAdmin(admin.ModelAdmin):
    model = Text