from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class GeneralInformation(Page):
    form_model = models.Player
    form_fields = ['gender', 'age_group', 'english_level']


class Results(Page):
    pass


page_sequence = [
    GeneralInformation,
    Results
]
