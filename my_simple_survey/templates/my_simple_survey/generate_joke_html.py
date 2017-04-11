from my_simple_survey.data.jokes import JOKES

if __name__ == "__main__":
    jokes = '\n\n'.join([
        """

      <p><strong>Question: </strong>""" + j['question'] + """</p>
      <p><strong>Answer: </strong>""" + j['answer'] + """</p>

      {% formfield player.joke_""" + str(i) + """ with label="" %}
      <br>
        """ for i, j in enumerate(JOKES, start=1)])

    html = """
    {% extends "global/Page.html" %}
    {% load staticfiles otree_tags %}

    {% block title %}
    Please, evaluate the following jokes
    {% endblock %}

    {% block content %}

    """ + jokes + """

    {% next_button %}


    {% endblock %}

    """

    with open('Joke.html', 'wb') as f:
        f.write(html.encode('utf8'))
