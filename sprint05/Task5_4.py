class ToSmallNumberGroupError(Exception):
    pass
def check_number_group(number):
    try:
        k = int(number)
        if int(number)>10:
            return f"Number of your group {number} is valid"
        else:
            raise ToSmallNumberGroupError
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError:
        return "We obtain error:Number of your group can't be less than 10"