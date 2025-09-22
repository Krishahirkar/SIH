from django.contrib import admin
from .models import Class, Subject, Chapter, Question, Option, MatchPair, Score

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class MatchPairInline(admin.TabularInline):
    model = MatchPair
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text_en', 'chapter', 'question_type')
    list_filter = ('question_type', 'chapter__subject__school_class')
    inlines = [OptionInline, MatchPairInline]

# Register your models here
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Score)