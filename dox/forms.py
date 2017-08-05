from django import forms
from django.utils.translation import ugettext_lazy as _
from dox import models

class PageForm(forms.ModelForm):
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'vLargeTextField',
            'rows': 50,
            'cols': 40,
        }),
        required=False,
    )
    
    # https://code.djangoproject.com/browser/django/trunk/django/contrib/flatpages/forms.py
    
    try:
        url = forms.RegexField(
            label=_('URL'),
            max_length=255,
            regex=r'^[-\w/\.~]+$',
            help_text = _(u'Example: /templates/ap/hosted2/ (leading/trailing slashes required)'),
            error_message = _(u'This value must contain only letters, numbers, dots, underscores, dashes, slashes or tildes.'),
        )
    except TypeError:
        # Django >= 1.6 'error_messages' dict rather than 'error_message' kw
        url = forms.RegexField(
            label=_('URL'),
            max_length=255,
            regex=r'^[-\w/\.~]+$',
            help_text = _(
                u'Example: /templates/ap/hosted2/ (leading/trailing slashes required)'
            ),
            error_messages = {
                'invalid': _(u'This value must contain only letters, numbers, dots, underscores, dashes, slashes or tildes.'),
            },
        )

    
    class Meta:
        model = models.Page
        # Added fields to keep Django >= 1.6 happy
        fields = (
            'name',
            'url',
            'template_name',
            'status',
            'is_active',
            'publish_date',
            'expiration_date',
            'login_required',
            'author',
            'notes',
            'head_title',
            'head_title_extra',
            'head_description',
            'head_keywords',
            'head_extra',
            'title',
            'content',
            'description_short',
            'description_long',
            'extra',
        )
