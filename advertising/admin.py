from django.contrib import admin
from django import forms

from advertising.models import *

class CustomAdForm(forms.ModelForm):
    active = forms.BooleanField() # make this manually there

    class Meta:
        model = Advertisement
        fields = (
            'title',
            'image',
            'url',
            'code',
            'position',
            'start_date',
            'end_date',
            'paid',
            'paid_views',
            'views'
        )

class AdAdmin(admin.ModelAdmin):
    #form = CustomAdForm
    readonly_fields = ('views',)

admin.site.register(Advertisement, AdAdmin)
