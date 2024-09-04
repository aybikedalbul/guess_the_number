# jinja2.py
from jinja2 import Environment, FileSystemLoader

def environment(**options):
    env = Environment(
        loader=FileSystemLoader('jinja_templates'),
        autoescape=True,
        **options
    )
    return env
