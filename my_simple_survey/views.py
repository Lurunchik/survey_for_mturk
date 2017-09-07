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


class SurveyCode(Page):
    form_model = models.Player


class Results(Page):
    pass


class Preview(Page):
    pass


class Result(Page):
    pass


class Joke1(Page):
    form_model = models.Player
    form_fields = ['joke_1', 'joke_2', 'joke_3']
    template_name = 'my_simple_survey/Joke1.html'


class Joke4(Page):
    form_model = models.Player
    form_fields = ['joke_4', 'joke_5', 'joke_6']
    template_name = 'my_simple_survey/Joke4.html'


class Joke7(Page):
    form_model = models.Player
    form_fields = ['joke_7', 'joke_8', 'joke_9']
    template_name = 'my_simple_survey/Joke7.html'


class Joke10(Page):
    form_model = models.Player
    form_fields = ['joke_10', 'joke_11', 'joke_12']
    template_name = 'my_simple_survey/Joke10.html'


class Joke13(Page):
    form_model = models.Player
    form_fields = ['joke_13', 'joke_14', 'joke_15']
    template_name = 'my_simple_survey/Joke13.html'


class Joke16(Page):
    form_model = models.Player
    form_fields = ['joke_16', 'joke_17', 'joke_18']
    template_name = 'my_simple_survey/Joke16.html'


class Joke19(Page):
    form_model = models.Player
    form_fields = ['joke_19', 'joke_20', 'joke_21']
    template_name = 'my_simple_survey/Joke19.html'


class Joke22(Page):
    form_model = models.Player
    form_fields = ['joke_22', 'joke_23', 'joke_24']
    template_name = 'my_simple_survey/Joke22.html'


class Joke25(Page):
    form_model = models.Player
    form_fields = ['joke_25', 'joke_26', 'joke_27']
    template_name = 'my_simple_survey/Joke25.html'


class Joke28(Page):
    form_model = models.Player
    form_fields = ['joke_28', 'joke_29', 'joke_30']
    template_name = 'my_simple_survey/Joke28.html'


page_sequence = [
    Preview,
    GeneralInformation,
    Joke1,
    Joke4,
    Joke7,
    Joke10,
    Joke13,
    Joke16,
    Joke19,
    Joke22,
    Joke25,
    Joke28,
    SenseOfHumor,
    Result,
]
