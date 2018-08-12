from otree.api import models, widgets


def get_agreement_field():
    return models.PositiveIntegerField(
        choices=[
            [1, 'Disagree strongly'],
            [2, 'Disagree moderately'],
            [3, 'Disagree a little'],
            [4, 'Neither agree nor disagree'],
            [5, 'Agree a little'],
            [6, 'Agree moderately'],
            [7, 'Agree strongly']
        ]
    )


def get_joke_field():
    return models.PositiveIntegerField(choices=[
        [1, '😞 не шутка'],
        [2, '😞 попытка пошутить'],
        [3, '😊 шутка'],
    ],
        min=1,
        max=3,
        widget=widgets.RadioSelectHorizontal(),
    )
