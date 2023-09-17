def maximo(number_one, number_tow, number_three):
    if number_one >= number_tow and number_one >= number_three:
        return number_one
    if number_tow >= number_one and number_tow >= number_three:
        return number_tow
    else:
        return number_three
