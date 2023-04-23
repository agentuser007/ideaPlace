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
