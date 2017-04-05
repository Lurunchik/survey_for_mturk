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
    english_level = models.PositiveIntegerField(
        choices=[
            [1, 'Poor'],
            [2, 'Average'],
            [3, 'Good'],
            [4, 'Bilingual'],
            [5, 'Native'],
        ]
    )


class HumanHumorSense(BasePlayer):
    _AGREEMENT_CHOICES = [
        [1, 'Disagree strongly'],
        [2, 'Disagree moderately'],
        [3, 'Disagree a little'],
        [4, 'Neither agree nor disagree'],
        [5, 'Agree a little'],
        [6, 'Agree moderately'],
        [7, 'Agree strongly']
    ]
    laugh = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    pun = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    extraverted = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    critical = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    dependable = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    anxious = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    complex = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    warm = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    disorganized = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    calm = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
    conventional = models.PositiveIntegerField(
        choices=_AGREEMENT_CHOICES
    )
