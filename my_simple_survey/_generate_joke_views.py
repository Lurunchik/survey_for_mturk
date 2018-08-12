import os
import re
from collections import namedtuple

from my_simple_survey.data.jokes import JOKES, JOKES_COUNT_ON_PAGE

JokeClass = namedtuple('JokeClass', ['name', 'body'])


#  я понимаю, что это полнейший говнокод,
#  но эта джанговская пежня не работает иначе

def _get_joke_class_code(j_id):
    return JokeClass(
        name="Joke{}".format(j_id),
        body="""
class Joke{id}(JokePage):
    template_name = 'my_simple_survey/Joke{id}.html'
""".format(id=j_id))


def get_jokes_files():
    for f in os.listdir("templates/my_simple_survey/"):
        if f.startswith('Joke'):
            yield f


if __name__ == "__main__":
    joke_ids = sorted(int(re.search(r'\d+', f).group())
                      for f in get_jokes_files())

    assert len(joke_ids) == len(JOKES), 'Joke counts do not match, you might want to run HTML generation first'

    with open('_view_template', 'r') as t, open('views.py', 'w') as f:
        j_classes = [_get_joke_class_code(j_id) for j_id in joke_ids]
        file = t.read()
        file += "\n".join(j.body for j in j_classes)

        page_sequence = """
page_sequence = [
    Preview,
    {},
]
""".format(',\n    '.join(j.name for j in j_classes))
        file += "\n" + page_sequence
        f.write(file)
