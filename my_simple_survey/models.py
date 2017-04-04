from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

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
    name = models.CharField()
    gender = models.PositiveIntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Prefer not to disclose'],
        ]
    )
    age_group = models.PositiveIntegerField(
        choices=[
            [1, '18-30'],
            [2, '31-40'],
            [3, '41-50'],
            [4, '51-60'],
            [5, '61+'],
        ], help_text='age group'
    )
