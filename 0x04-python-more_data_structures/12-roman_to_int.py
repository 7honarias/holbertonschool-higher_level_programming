#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string.isalpha() or roman_string is not None:
        dic_roman = {"X": 10, "I": 1, "V": 5, "C": 100, "L": 50, "D": 500}
        result = 0
        temp = 0
        for str in roman_string:
            value = dic_roman[str]
            if temp >= value or temp == 0:
                result += value
            else:
                result = value + result - (temp * 2)
            temp = value
        return(result)
    return (0)
