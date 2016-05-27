from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='splitter')
@stringfilter
def splitter(value, arg):
    '''
    Improved splitter tag in that it doesn't strip out the string being split 
    on and doesn't add that string to the last item (where it doesn't belong!) 
    as a list comprehension would do.
    '''
    outlist = []
    split_list = value.split(arg)
    graf_count = len(split_list)
    for index, item in enumerate(split_list):
        if (index + 1) < graf_count:
            item = item + u'</p>'
            outlist.append(item)
        else:
            outlist.append(item)
    return outlist
