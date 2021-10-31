def day_of_week(day):
    week_days = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5, "Saturday":6, "Sunday":7}
    try:
        if int(day) in week_days.values():
            for key, value in week_days.items():
                if int(day) == value:
                    return key
            else:
                return "There is no such day of the week! Please try again."
    except TypeError:
        return "You did not enter a number! Please try again."