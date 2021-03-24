from django.contrib import admin

from .models import Questions, Responses, Survey


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'create')
    list_filter = ('create',)
    search_fields = ('question',)
    prepopulated_fields = {'slug': ('question',)}


@admin.register(Responses)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'question', 'create')
    list_filter = ('name', 'create')
    search_fields = ('question', 'answer')


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'slug',)
    list_display_links = ('id', 'title')
    list_filter = ('create',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

