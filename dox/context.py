from django.core.urlresolvers import resolve, Resolver404
'''
Based on:
1.) http://stackoverflow.com/questions/20020911/how-to-get-the-name-of-current-app-within-a-template
2.) http://stackoverflow.com/questions/11232017/django-extend-template-by-return-value-of-template-tag
3.) http://stackoverflow.com/questions/7363291/django-resolverequest-path-app-name-does-not-return-app-name/7363786#7363786

Once you add "dox.context.app_label", to TEMPLATE_CONTEXT_PROCESSORS in 
settings.py, this lights up the {{ app_label }} template variable everywhere 
you have a ContextRequest kind of response. Handy variable to have in the 
ChartBeat and Parsely JavaScripts.

'''

def app_label(request):
    try: 
        app_label = resolve(request.path).app_name
    except Resolver404:
        app_label = None
    return {
        'app_label': app_label
    }
