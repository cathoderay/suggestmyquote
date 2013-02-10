from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache

from quotes import quotes
from core import get_quote


@never_cache
def home(request):
    quote, author = get_quote()
    return render_to_response('index.html', {'quote': quote, 
                                             'author': author, 
                                             'number': len(quotes)})

