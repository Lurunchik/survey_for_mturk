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

score_counts = collections.defaultdict(int)
for joke in jokes:
    if joke.id in joke_scores_aggregated:
        scores = sorted(joke_scores_aggregated[joke.id])
        score_counts[len(scores)] += 1

        median = len(scores) // 2

        if len(scores) % 2 == 0:
            score = (scores[median] + scores[median - 1]) / 2
        else:
            score = scores[median]

        if joke.is_joke:
            total_joke_count += 1
            if score >= 2:
                true_joke_count += 1
        else:
            total_non_joke_count += 1
            if score < 2:
                true_non_joke_count += 1

print(f'Jokes assessed: {total_joke_count}, true: {true_joke_count}\n'
      f'Percentage: {true_joke_count / total_joke_count}')

print(f'Non-jokes assessed: {total_non_joke_count}, true: {true_non_joke_count}\n'
      f'Percentage: {true_non_joke_count / total_non_joke_count}')

for score, count in score_counts.items():
    print(f'{score} scores: {count}')
