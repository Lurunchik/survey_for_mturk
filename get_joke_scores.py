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
    joke_scores_aggregated[score.joke].append(score.score)

print(len(joke_scores_aggregated))

true_joke_count = 0
true_non_joke_count = 0
total_joke_count = 0
total_non_joke_count = 0
for joke in jokes:
    if joke.id in joke_scores_aggregated:
        scores = joke_scores_aggregated[joke.id]
        score = sum(scores) / len(scores)
        if joke.is_joke:
            total_joke_count += 1
            if score >= 2:
                true_joke_count += 1
        else:
            total_non_joke_count += 1
            if score < 1:
                true_non_joke_count += 1

print(f'Jokes assessed: {total_joke_count}, true: {true_joke_count}\n'
      f'Percentage: {true_joke_count / total_joke_count}')

print(f'Non-jokes assessed: {total_non_joke_count}, true: {true_non_joke_count}\n'
      f'Percentage: {true_non_joke_count / total_non_joke_count}')
