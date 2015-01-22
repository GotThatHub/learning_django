from django.http import HttpResponse
from django.shortcuts import render
#from django.template.loader import get_template
#from django.template import Context
import datetime


def hello(request):
    return HttpResponse("Hello world")

def home(request):
    return HttpResponse("<a href=time/>I think I get it</a>")

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #c = Context({'current_date':now})
    #html = t.render(c)
    #return HttpResponse(html)
    return render(request,'current_datetime_child.html',{'current_date':now})

def hours_ahead(request, offset):

    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead_child.html', {'hours_ahead':offset,'new_time':dt})
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)

def test_anti(request):
    import antigravity
    return HttpResponse("<html><p>Did it work?</p></html>")

def my_test(request, answer="yes"):
    from django import template

    html_code = '''This is so {{ description }}'''

    context_vars = {'description' : 'fucking cool'}

    c = template.Context(context_vars)
    t = template.Template(html_code)

    return HttpResponse(t.render(c))
