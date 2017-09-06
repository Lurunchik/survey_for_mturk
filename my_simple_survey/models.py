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

    @staticmethod
    def jester_jokes_by_id():
        return {i: j for i, j in enumerate(JOKES[0:7], start=1)}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class HumorTypes(enum.IntEnum):
    DID_NOT_GET_IT = 0
    AVERAGE = 1
    HIGH_FUNNY = 2


class Player(BasePlayer):
    most_diff_joke = None
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
        return [x - 1 for x in
                [self.joke_1, self.joke_2, self.joke_3, self.joke_4,
                 self.joke_5, self.joke_6, self.joke_7]]

    def __evaluate_user(self):
        laugh_more_often_than = defaultdict(int)
        laugh_rarer_than = defaultdict(int)
        for i, label in enumerate(self.user_labels(), start=1):
            laugh_more_often_than[label] += sum(
                Constants.jokes_avarage_evaluation[i][l]
                for l in range(0, label)
            )
            laugh_rarer_than[label] += sum(
                Constants.jokes_avarage_evaluation[i][l]
                for l in range(label + 1, 4)
            )

        def norm(x):
            return sum(x.values()) / 7

        return norm(laugh_more_often_than), norm(laugh_rarer_than)

    def result(self):
        def percent(x):
            return round(x * 100)

        often_than, rarer_than = self.__evaluate_user()
        res = {
            HumorTypes.DID_NOT_GET_IT:
                "Only {}% of the other participants find jokes to be funny "
                "less often than you.".format(percent(rarer_than))
        }.get(
            self._user_type(),
            "You find jokes to be funny more often than {}% "
            "of the other participants".format(percent(often_than))
        )

        return res

    def __get_most_diff_joke(self):
        if not self.most_diff_joke:
            max_diff = defaultdict(int)
            diff_jokes = defaultdict(dict)

            for i, label in enumerate(self.user_labels(), start=1):
                max_bath = max(Constants.jokes_avarage_evaluation[i].items(),
                               key=operator.itemgetter(1))
                if max_bath[1] != label:
                    diff = max_bath[1] - Constants.jokes_avarage_evaluation[i][
                        label]
                    if diff > max_diff[label]:
                        diff_jokes[label] = {
                            'label': label,
                            'id': i,
                            'majority_label': max_bath[0],
                            'diff': round(diff * 100)}
                        max_diff[label] = diff
            max_diff = round(max(max_diff.values()) * 100)
            self.most_diff_joke = next(
                v for v in diff_jokes.values() if v['diff'] == max_diff)
        return self.most_diff_joke

    def diff_joke_text(self):
        joke = Constants.jester_jokes_by_id()[self.__get_most_diff_joke()['id']]
        return joke

    def _user_type(self):
        user_score = sum(self.user_labels())
        diff = user_score - Constants.average_score()
        if abs(diff) < 5:
            return HumorTypes.AVERAGE
        if diff < 0:
            return HumorTypes.DID_NOT_GET_IT
        if diff > 0:
            return HumorTypes.HIGH_FUNNY

    def result_type(self):
        '''
        min diff: 1
        max_diff: 40
        :return:
        '''
        return int(self._user_type())

    def has_chart(self):
        joke = self.__get_most_diff_joke()
        return joke and joke['diff'] > 3

    def chart(self):
        not_funny = 'not funny at all'
        can_be_better = 'can be better'
        funny = 'funny'
        hilarious = 'hilarious'
        label_by_pic = {not_funny: 0, can_be_better: 1, funny: 2, hilarious: 3}
        template = [{
            'name': 'Marks',
            'colorByPoint': True,
            'data': [{
                'name': not_funny,
                'y': 0,
            }, {
                'name': can_be_better,
                'y': 0,
            }, {
                'name': funny,
                'y': 0,
            }, {
                'name': hilarious,
                'y': 0
            }]
        }]

        joke = self.__get_most_diff_joke()

        joke_scores = Constants.jokes_avarage_evaluation[joke['id']]
        for data in template[0]['data']:
            data['y'] = joke_scores[label_by_pic[data['name']]]
            if joke['label'] == label_by_pic[data['name']]:
                data['sliced'] = True
                data['selected'] = True
                data['name'] += ' ' \
                                '(Your are here!!!)'

        return template
