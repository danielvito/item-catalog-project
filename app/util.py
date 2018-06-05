from flask import make_response
import pprint
import inspect


class Util:

    def print(variable, indent=6, width=1):
        if hasattr(variable, '__dict__'):
            print(pprint.pformat(vars(variable), indent=indent, width=width))
        else:
            pp = pprint.PrettyPrinter(indent=indent)
            pp.pprint(variable)

    def custom_make_response(text, code):
        response = make_response(text, code)
        response.headers['Content-Type'] = 'application/json'
        return response
