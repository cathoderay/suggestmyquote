import random

from django.shortcuts import render_to_response, redirect
from django.views.decorators.cache import never_cache

from core import get_quote, get_number



def get_random():
    return random.randint(0, get_number() - 1)


@never_cache
def home(request):
    id = get_random()
    return redirect('/quote/%d' % id)


def quote(request, id):
    try:
        id = int(id)
    except:
        id = get_random() 
    quote, author = get_quote(id)
    return render_to_response('index.html', {'quote': quote, 
                                             'author': author, 
                                             'number': get_number()})
    
