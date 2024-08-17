from django import template
import re

register = template.Library()

@register.filter(name='nl2br')
def nl2br(value):
    if not value:
        return ''
    # Replace newline characters with <br>
    return re.sub(r'\r\n|\r|\n', '<br>', value)