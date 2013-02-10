import random

from quotes import quotes


def get_quote():
    return random.choice(quotes)
