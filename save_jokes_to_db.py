import os
import django

from my_simple_survey.data.jokes import JOKES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from my_simple_survey.models import Joke

for i, joke in enumerate(JOKES, start=1):
    Joke.objects.create(id=i, text=joke)
