import random
from django import template

register = template.Library()

@register.simple_tag
def get_adicio_widget():
    '''
    Usage: {% adicio_widget %}
    
    Returns Adicio widget <iframe></iframe>
    '''
    adicio_categories = (
        "autos",
        "homes",
        "jobs",
        )
    random_category = random.choice(adicio_categories)
    widget_html = '''<div class="advert">
        <iframe src="http://advertising.registerguard.com/p/marketplace/{0}/" frameborder="0" width="300" height="525" scrolling="no"></iframe>
    </div>'''.format(random_category,)

    return widget_html
