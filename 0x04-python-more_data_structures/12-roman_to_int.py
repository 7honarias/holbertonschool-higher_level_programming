#!/usr/bin/python3
def roman_to_int(roman_string):

    if isinstance(roman_string, str):
        dic_roman = {
            "X": 10, "I": 1, "V": 5, "C": 100, "L": 50, "D": 500, "M": 1000}
        result = 0
        temp = 0
        for sr in roman_string:
            value = dic_roman[sr]
            if temp >= value or temp == 0:
                result += value
            else:
                result = value + result - (temp * 2)
            temp = value
        return(result)
    return (0)
