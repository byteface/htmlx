"""
    htmlx.decorators
    ====================================

"""

import functools
import warnings
from functools import wraps
from typing import Callable


def el(element="div", string: bool = False):
    """[wraps the results of a function in an element]"""

    if isinstance(element, str):
        from htmlx.dom import Document

        element = Document.createElement(element).__class__

    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if string == False:
                return element(result)
            else:
                return str(element(result))

        return wrapper

    return decorator


def silence(*args, **kwargs):
    """stop a function from doing anything"""

    def dont_do_it(f):
        return None

    return dont_do_it


def as_json(func):
    """decorate any function to return json instead of a python obj
    note - used by JSON.py
    """

    def JSON_decorator(*args, **kwargs):
        import json

        return json.dumps(func(*args, **kwargs))

    return JSON_decorator
