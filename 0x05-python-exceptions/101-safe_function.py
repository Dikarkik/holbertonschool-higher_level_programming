#!/usr/bin/python3


def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
    return result
