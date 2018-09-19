import collections
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from my_simple_survey.models import Joke, JokeScore


jokes = Joke.objects.all()
joke_scores = JokeScore.objects.all()

joke_scores_aggregated = collections.defaultdict(list)
for score in joke_scores:
    joke_scores_aggregated[score.joke].append((score.score, score.player))

for joke in jokes:
    if joke.id in joke_scores_aggregated:
        print(joke.text)
        print(joke.is_joke)
        print(joke_scores_aggregated[joke.id])
