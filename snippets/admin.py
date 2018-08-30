from django.contrib import admin

from snippets.models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'style')

    class Meta:
        model = Snippet
        fields = '__all__'
