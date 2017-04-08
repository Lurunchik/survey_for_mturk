from my_simple_survey.data.jokes import JOKES
from . import models
from ._builtin import Page


class GeneralInformation(Page):
    form_model = models.Player
    form_fields = ['gender', 'age_group', 'english_level']


class SenseOfHumor(Page):
    form_model = models.Player
    form_fields = ['laugh', 'pun', 'extraverted', 'critical', 'dependable',
                   'anxious', 'complex', 'warm', 'disorganized', 'calm',
                   'conventional']


class BaseJoke(Page):
    form_model = models.Player
    template_name = 'my_simple_survey/Joke.html'


class Joke(BaseJoke):
    form_fields = ['joke_{}'.format(i) for i in range(1, len(JOKES) + 1)]


def get_joke_page(joke_id: int):
    assert joke_id < len(JOKES), '{} is wrong joke id'.format(joke_id)
    form_field = 'joke_{}'.format(joke_id)

    def set_vars_for_template():
        return {'joke': JOKES[joke_id],
                'field': getattr(models.Player, form_field)
                }

    return type(
        'Joke', (BaseJoke,),
        {
            'vars_for_template': set_vars_for_template,
            'form_fields': [form_field]
        }
    )


class Results(Page):
    pass


page_sequence = [
    Joke,
    # GeneralInformation,
    # SenseOfHumor,
    Results
]
