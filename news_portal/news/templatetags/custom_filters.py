from django import template
register = template.Library()

bad_words = [
    'айтишник'
]

@register.filter()
def censor(value):
    for bw in bad_words:
     value = value.lower().replace(bw.lower(), '***')
    return value

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()