from my_simple_survey.data.jokes import JOKES, JOKES_COUNT_ON_PAGE


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_html(jokes, start_id):
    jokes_html = '\n\n'.join(
[
"""<p><strong>Question: </strong>""" + j['question'] + """</p>
<p><strong>Answer: </strong>""" + j['answer'] + """</p>
{% formfield player.joke_""" + str(i) + """ with label="" %}
<br>
""" for i, j in enumerate(jokes, start=start_id)
            ])

    html = """{% extends "global/Page.html" %}
{% load staticfiles otree_tags %}

{% block content %}
<h3>Please, evaluate the following jokes </h3>
""" + jokes_html + """
{% next_button %}


{% endblock %}
"""
    return html.encode('utf8')


if __name__ == "__main__":

    i = 1
    for t in chunks(JOKES, JOKES_COUNT_ON_PAGE):
        with open('Joke{}.html'.format(i), 'wb') as f:
            f.write(get_html(t, i))
            i = i + len(t)
