def check_odd_even(number):
    try:
        if number%2:
            return "Entered number is odd"
        else:
            return "Entered number is even"
    except:
        return "You entered incorrect data. Please try again."