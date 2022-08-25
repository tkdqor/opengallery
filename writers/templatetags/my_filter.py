from django import template

register = template.Library()


def my_filter(value):
    count = 0
    if value.size <= 100:
        count += 1
    return count
