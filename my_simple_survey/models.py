from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    gender = models.PositiveIntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Prefer not to disclose'],
        ],
        widget=widgets.RadioSelect()
    )
    age_group = models.PositiveIntegerField(
        choices=[
            [1, '18-30'],
            [2, '31-40'],
            [3, '41-50'],
            [4, '51-60'],
            [5, '61+'],
        ],
        widget=widgets.RadioSelect()
    )
    english_level = models.PositiveIntegerField(
        choices=[
            [1, 'Poor'],
            [2, 'Average'],
            [3, 'Good'],
            [4, 'Bilingual'],
            [5, 'Native'],
        ]
    )

    laugh = get_agreement_field()
    pun = get_agreement_field()
    extraverted = get_agreement_field()
    critical = get_agreement_field()
    dependable = get_agreement_field()
    anxious = get_agreement_field()
    complex = get_agreement_field()
    warm = get_agreement_field()
    disorganized = get_agreement_field()
    calm = get_agreement_field()
    conventional = get_agreement_field()

    joke_1 = get_joke_field()
    joke_2 = get_joke_field()
    joke_3 = get_joke_field()
    joke_4 = get_joke_field()
    joke_5 = get_joke_field()
    joke_6 = get_joke_field()
    joke_7 = get_joke_field()
    joke_8 = get_joke_field()
    joke_9 = get_joke_field()
    joke_10 = get_joke_field()
    joke_11 = get_joke_field()
    joke_12 = get_joke_field()
    joke_13 = get_joke_field()
    joke_14 = get_joke_field()
    joke_15 = get_joke_field()
    joke_16 = get_joke_field()
    joke_17 = get_joke_field()
    joke_18 = get_joke_field()
    joke_19 = get_joke_field()
    joke_20 = get_joke_field()
    joke_21 = get_joke_field()
    joke_22 = get_joke_field()
    joke_23 = get_joke_field()
    joke_24 = get_joke_field()
    joke_25 = get_joke_field()
    joke_26 = get_joke_field()
    joke_27 = get_joke_field()
    joke_28 = get_joke_field()
    joke_29 = get_joke_field()
    joke_30 = get_joke_field()
