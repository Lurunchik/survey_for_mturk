from otree.api import Currency as c, currency_range
from otree.common import safe_json

from my_simple_survey.jokes import JOKES
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class GeneralInformation(Page):
    form_model = models.Player
    form_fields = ['gender', 'age_group', 'english_level']


class SenseOfHumor(Page):
    form_model = models.Player
    form_fields = ['laugh', 'pun', 'extraverted', 'critical', 'dependable',
                   'anxious', 'complex', 'warm', 'disorganized', 'calm',
                   'conventional']


class Jokes(Page):
    form_model = models.Player
    form_fields = ['joke_1']

    def vars_for_template(self):
        return {'jokes': safe_json(JOKES)}


class Results(Page):
    pass


page_sequence = [
    Jokes,
    # GeneralInformation,
    # SenseOfHumor,
    Results
]
