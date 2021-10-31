class MyError(Exception):
    pass


def check_positive(number):
    try:
        if float(number) >= 0:
            return (f"You input positive number: {float(number)}")
        else:
            raise MyError
    except MyError:
        return (f"You input negative number: {float(number)}. Try again.")
    except ValueError:
        return ("Error type: ValueError!")