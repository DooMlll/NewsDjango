from django import template


register = template.Library()



words = ['редиска', 'какашка', 'слоупок']

@register.filter()
def censor(value):
    for word in words:
        value = value.replace(word, '***')
        return value

    else:
        return value