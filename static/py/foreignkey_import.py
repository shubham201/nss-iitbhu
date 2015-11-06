import re
from __future__ import unicode_literals
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.forms.fields import Field, FileField
from django.forms.utils import ErrorDict, ErrorList, flatatt
from django.forms.widgets import Media, MediaDefiningClass, Textarea, TextInput
from django.utils import six
from django.utils.encoding import (
    force_text, python_2_unicode_compatible, smart_text,
)
from django.utils.functional import cached_property
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

__all__ = ('MyForm', 'BaseForm')

class MyForm(object):