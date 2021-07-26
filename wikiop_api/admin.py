from django import forms
from django.contrib import admin
from .models import ProjectExample,PrimarySection,SecondarySection,FixedSection,QuestionAndAnswer


admin.site.site_header = "WIKIOP MANAGER"
admin.site.site_title = "WIKIOP MANAGER"

class QuestionAndAnswerAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
    list_display = ('question','primary_section','secondary_section',)
    list_filter = ("primary_section",)

class SecondarySectionAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
    list_display = ('name','primary_section')
    list_filter = ("primary_section",)


admin.site.register(ProjectExample)
admin.site.register(PrimarySection)
admin.site.register(SecondarySection,SecondarySectionAdmin)
admin.site.register(FixedSection)
admin.site.register(QuestionAndAnswer,QuestionAndAnswerAdmin)