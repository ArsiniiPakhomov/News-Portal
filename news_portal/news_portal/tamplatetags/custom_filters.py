from django import template
register = template.library()

bad_words = [
    'айтишник'
]

@register.filter()
def censor(value):
    for bw in bad_words:
     value = value.lower().replace(bw.lower(), '***')
    return value

    