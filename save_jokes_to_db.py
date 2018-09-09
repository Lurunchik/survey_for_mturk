import os
import random

import django

from my_simple_survey.data.jokes import JOKES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from my_simple_survey.models import Joke

jokes = list(JOKES)
random.shuffle(jokes)
for i, joke in enumerate(jokes, start=1):
    Joke.objects.create(id=i, text=joke, is_joke=bool(JOKES[joke]))
