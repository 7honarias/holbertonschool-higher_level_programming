#!/usr/bin/python3
"""matrix_mul init"""


def matrix_mul(m_a, m_b):
    """ multiplies 2 matrices"""

    a = 0
    b = 0
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) < 1:
        raise TypeError("m_a can't be empty")
    if len(m_b) < 1:
        raise TypeError("m_b can't be empty")

    for i in m_a:
        if len(i) < 1:
            raise ValueError("m_a can't be empty")
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        for x in i:
            if type(x) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
        if a == 0:
            a = len(i)
        if len(i) != a:
            raise TypeError("each row of m_a must be of the same size")

    for i in m_b:
        if len(i) < 1:
            raise ValueError("m_b can't be empty")
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        for x in i:
            if type(x) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
        if b == 0:
            b = len(i)
        if len(i) != b:
            raise TypeError("each row of m_b must be of the same size")

    if a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m = 0
    suma = 0
    x = 0
    y = 0
    m_r = []
    my_list = []
    while m < len(m_a):
        my_list = []
        x = 0
        while x < a:
            y = 0
            suma = 0
            while y < a:
                suma += m_a[m][y] * m_b[y][x]
                y += 1
            my_list.append(suma)
            x += 1
        m_r.append(my_list)
        m += 1

    return (m_r)
