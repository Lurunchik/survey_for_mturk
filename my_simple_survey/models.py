import enum
import operator
import random
from collections import defaultdict

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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class HumorTypes(enum.IntEnum):
    DID_NOT_GET_IT = 0
    AVERAGE = 1
    HIGH_FUNNY = 1


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
    code = models.PositiveIntegerField()
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

    def secret_code(self):
        self.code = random.randint(1, 1000000)
        return self.code

    def user_labels(self):
        return [self.joke_1, self.joke_2, self.joke_3, self.joke_4,
                self.joke_5, self.joke_6, self.joke_7]

    def __evaluate_user(self):
        eval_dict = defaultdict(int)
        for i, label in enumerate(self.user_labels(), start=1):
            eval_dict[label] += Constants.jokes_avarage_evaluation[i][label]

        return sum(eval_dict.values()) / 7

    def result(self):
        return round(self.__evaluate_user() * 100)

    def __get_diff_with_avg(self):
        max_diff = defaultdict(int)
        diff_jokes = defaultdict(dict)

        for i, label in enumerate(self.user_labels(), start=1):
            max_bath = max(Constants.jokes_avarage_evaluation[i].items(),
                           key=operator.itemgetter(1))
            if max_bath[1] != label:
                diff = max_bath[1] - Constants.jokes_avarage_evaluation[i][label]
                if diff > max_diff[label]:
                    diff_jokes[label] = {
                        'label': label,
                        'joke_id': i,
                        'majority_label': max_bath[0],
                        'diff': round(diff * 100)}
                    max_diff[label] = diff
        return diff_jokes, round(max(max_diff.values()) * 100)

    def _user_type(self):
        user_score = sum(self.user_labels())
        diff = user_score - Constants.average_score()
        if abs(diff) < 5:
            return HumorTypes.AVERAGE
        if diff < 0:
            return HumorTypes.DID_NOT_GET_IT
        if diff > 0:
            return HumorTypes.HIGH_FUNNY

    def result_text(self):
        '''
        min diff: 1
        max_diff: 40
        :return:
        '''
        return {
            HumorTypes.AVERAGE:
                """Great Job!
                    Your sense of Humor is:

Just right!

You're friendly and funny, interesting and able to smile genuinely. You tend to give great advice, but you shouldn't get offended too easily.""",
            HumorTypes.DID_NOT_GET_IT: """
            Great Job!
            Your sense of Humor is:
you don't get it!
It's ok, you'll get the hang of it, but keep trying. 
A lot of people may make fun of you, but try to stand up for yourself! 
Don't let little things get you down, you're sweet, cute, loyal and basically like a fluffy bunny.
            """,
            HumorTypes.HIGH_FUNNY: """
            Great Job!
            Your sense of Humor is:

Extreme
You tend to be bouncy, fun and very optimistic, a good friend and a huge laugh! You can always make someone smile, but CALM DOWN! You're too hyper! Sometimes you go a bit too far too impress people or yourself. You don't need humor ALL the time. Profile D"""
        }.get(self._user_type())

    def has_chart(self):
        diff, max_diff = self.__get_diff_with_avg()
        return diff and max_diff > 3

    def chart(self):
        label_by_pic = {'😞': 0, '😔': 1, '😊': 2, '😆': 3}
        template = [{
            'name': 'Marks',
            'colorByPoint': True,
            'data': [{
                'name': '😞',
                'y': 0,
            }, {
                'name': '😔',
                'y': 0,
            }, {
                'name': '😊',
                'y': 0,
            }, {
                'name': '😆',
                'y': 0
            }]
        }]
        diff, max_diff = self.__get_diff_with_avg()

        joke = next(v for v in diff.values() if v['diff'] == max_diff)

        joke_scores = Constants.jokes_avarage_evaluation[joke['joke_id']]
        for data in template[0]['data']:
            data['y'] = joke_scores[label_by_pic[data['name']]]
            if joke['label'] == label_by_pic[data['name']]:
                data['sliced'] = True
                data['selected'] = True
                data['name'] += ' - Your answer here!!!'

        return template
