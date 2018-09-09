from my_simple_survey.data.jokes import JOKES, JOKES_COUNT_ON_PAGE


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_html():
    return """<div class="jumbotron  jumbotron-fluid"><p>{{ player.joke_text }}</p>
{% formfield player.joke_score with label="" %}
<br>
</div>"""


if __name__ == "__main__":

    start_page_num = 1
    joke_chunks = list(chunks(JOKES, JOKES_COUNT_ON_PAGE))
    max_pages = len(joke_chunks) + 1
    for i, t in enumerate(joke_chunks, start=1):
        with open('Joke{}.html'.format(start_page_num), 'wb') as f:
            content_block = """
<h3>Пожалуйста, оцените, является ли текст ниже шуткой: </h3> 
            {html}""".format(
                html=get_html())
            html = """{% extends "global/Page.html" %}
                {% load staticfiles otree_tags %}

                {% block content %}
                """ + content_block + """
                {% next_button %}

                {% endblock %}
            """
            f.write(html.encode('utf-8'))
        start_page_num += len(t)
