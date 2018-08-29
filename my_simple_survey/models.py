import enum
import operator
import random
from collections import defaultdict
from django import forms
from django.db.models import Count
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)
from otree.models.varsmixin import ModelWithVars

from my_simple_survey.data.jokes import JOKES
from my_simple_survey.fields import get_agreement_field, get_joke_field

author = 'lurunchik_chomechome'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'humor_evaluation'
    players_per_group = None
    num_rounds = 1
    instructions_template = 'my_simple_survey/Instructions.html'
    jokes_avarage_evaluation = {
        1: {0: 0.168492844365, 1: 0.258161896243, 2: 0.332737030411,
            3: 0.24060822898},
        2: {0: 0.158314669653, 1: 0.245847331094, 2: 0.349570735349,
            3: 0.246267263904},
        3: {0: 0.314421844971, 1: 0.303090967329, 2: 0.264533952594,
            3: 0.117953235106},
        4: {0: 0.0797783354245, 1: 0.127770807194, 2: 0.311062317022,
            3: 0.48138854036},
        5: {0: 0.123842343313, 1: 0.191794098643, 2: 0.339004953694,
            3: 0.345358604351},
        6: {0: 0.0753479811342, 1: 0.163464856781, 2: 0.398596571954,
            3: 0.36259059013},
        7: {0: 0.208615948671, 1: 0.270210815765, 2: 0.327314390467,
            3: 0.193858845096}
    }

    def __get_jokes_borders(self):
        max_diff, min_diff = 0, 100

        for i, v in self.jokes_avarage_evaluation.items():
            m_diff = max(v.values()) - min(v.values())
            if m_diff > max_diff:
                max_diff = m_diff
            min_d = max(v.values()) - sorted(v.values(), reverse=True)[1]
            if min_d and min_d < min_diff:
                min_diff = min_d
        return min_diff, max_diff

    @staticmethod
    def average_score():
        return sum(max(Constants.jokes_avarage_evaluation[i].items(),
                       key=operator.itemgetter(1))[0]
                   for i, v in Constants.jokes_avarage_evaluation.items())

    @staticmethod
    def jester_jokes_by_id():
        return {i: j for i, j in enumerate(JOKES[0:7], start=1)}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    joke_score = models.PositiveIntegerField(choices=[
        [1, '😞 не шутка'],
        [2, '😔 попытка пошутить'],
        [3, '😊 шутка'],
    ],
        min=1,
        widget=widgets.RadioSelectHorizontal(),
        max=3,
    )
    joke_id = models.PositiveIntegerField()

    def joke_text(self):
        jokes_left = Joke.objects.raw(
            """
              select e.id, text from (
     (select *
         from my_simple_survey_joke
         where id not in
               (select joke
                from my_simple_survey_jokescore
                where player = {player})
        ) w left join

        (
           select
             joke as jid,
             count(*) as count
           from my_simple_survey_jokescore
           group by joke
         ) q
      on (q.jid = w.id)
  )e order by count;
            """.format(player=self.id)
        )
        joke = jokes_left[0]

        self.joke_id = joke.id
        return joke.text


class Joke(ModelWithVars):
    class Meta:
        ordering = ['pk']
        app_label = 'my_simple_survey'

    id = models.PositiveIntegerField(primary_key=True, null=False)
    text = models.CharField()


class JokeScore(ModelWithVars):
    class Meta:
        ordering = ['pk']
        app_label = 'my_simple_survey'
        unique_together = (("player", "joke"),)

    player = models.PositiveIntegerField(null=False)
    joke = models.PositiveIntegerField(null=False)
    score = models.PositiveIntegerField(null=False)
