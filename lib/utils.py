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

