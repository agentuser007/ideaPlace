from django.db.models import Count
from django.shortcuts import render
from ideas.models import Idea

def obj_to_string(obj):
    """
    Convert an object to a string representation.
    """
    if isinstance(obj, str):
        return obj
    elif hasattr(obj, '__str__'):
        return str(obj)
    else:
        return repr(obj)

def truncate_text(text, length):
    """
    Truncates the given text to the specified length and appends "..." to the end.
    """
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text

def get_top_ideas(n):
    """
    Returns the top n ideas based on the number of likes.
    """
    ideas = Idea.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:n]
    return ideas
