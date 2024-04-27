"""
Напишите функцию last_discharge(a), которая в качестве аргумента получает строку, содержащую число a,
 и возвращает это же число, уменьшенное на единицу в последнем его разряде в виде строки.

Обратите внимание:

●     в последнем разряде может быть ноль,

●     входная строка может представлять как целое число, так и число с плавающей точкой,

●     входная строка содержит число строго больше нуля.
"""


# So the user enters the string and it decreases the last position by 1 and returns the number
def last_discharge(entrystring):
    carry = 1
    res = []

    pointer = len(entrystring) - 1
    while pointer > -1 and carry > 0:
        digit = entrystring[pointer]
        if digit == '.':
            pass
        elif digit == '0':
            digit = '9'
        else:
            carry = 0
            digit = str(int(digit) - 1)
        res.append(digit)
        pointer -= 1

    return entrystring[:pointer + 1] + ''.join(res[::-1])
    # Just creating a string  with +1 space more than the pointer and the appending the reversed string


if __name__ == '__main__':
    print(last_discharge('1.0'))  # Output: '0.9'
    print(last_discharge('1.00'))
    print(last_discharge('42'))  # Output: '41.0'
