from django import template
import datetime



register = template.Library()

@register.filter(name='index')
def index(indexable, i):
    return indexable[i]

@register.filter(name='indexparsed')
def indexparsed(indexable, i):
    return parse_date(str(indexable[i]))

def parse_date(date):
    if ':' in date and 'x' not in date:
        result = datetime.datetime.strptime(date, ('%Y-%m-%d %H:%M:00')).strftime('%H:%M')
    else:
        result = 'x'
    return result