import re


def valid_email(email):
    try:
        if re.fullmatch('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]', email):
            return ("Email is valid")

        else:
            raise ValueError
    except ValueError:
        return ("Email is not valid")