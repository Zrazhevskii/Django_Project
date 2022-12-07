from django.contrib import admin

from .models import Article, ArticleTag, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):

    def clean(self):
        checked = 0
        for form in self.forms:

            if form.cleaned_data.get('is_main') is True:
                checked += 1

        if checked > 1:
            raise ValidationError('Основным может быть только один раздел')

        elif checked == 0:
            raise ValidationError('Укажите основной раздел')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleTag
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ScopesAdmin(admin.ModelAdmin):
    pass
