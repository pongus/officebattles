from django import template

register = template.Library()


@register.filter(name='team')
def filter_teams(value, arg):
    if arg == 'home':
        is_home = True
    elif arg == 'away':
        is_home = False

    return value.filter(is_home=is_home)
