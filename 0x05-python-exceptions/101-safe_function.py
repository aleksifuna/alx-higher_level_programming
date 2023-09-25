#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as e:
        msg = "Exception: {}\n".format(str(e))
        sys.stderr.write(msg)
        return None
