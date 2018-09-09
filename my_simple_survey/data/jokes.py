import json
import os


JOKES_COUNT_ON_PAGE = 1

current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'examples_to_assess_new.json'), encoding='utf8') as f:
    JOKES = json.load(f)
