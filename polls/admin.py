from django.contrib import admin
from .models import Choice, Question, Tag

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Tags', {'fields': ['tags']}),
    ]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently','get_tag')
    search_fields = ['question_text']
    autocomplete_fields = ['tags']
    def get_tag(self, obj):
        return ", ".join([p.tag_name for p in obj.tags.all()])
    class Meta:
        model= Question

class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag_name'] 
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.filter(is_active=True)         
        return queryset, use_distinct

       
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Tag, TagAdmin)
