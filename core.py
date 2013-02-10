import random

from quotes import quotes


def get_number():
    return len(quotes)


def get_quote(id):
    return quotes[id]
