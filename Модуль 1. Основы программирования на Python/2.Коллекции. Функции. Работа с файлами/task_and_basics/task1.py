"""
Напишите функцию fibonacci(index), которая находит число Фибоначчи с нужным номером. Аргумент функции
index — целое положительное число.

Последовательность Фибоначчи задается формулой:

F(1) = 0

F(2) = 1

F(N) = F(N - 1) + F(N - 2) для N >= 3
То есть, каждое последующее число равно сумме двух предыдущих чисел. Если требуется больше информации о
данной последовательности, вы можете обратиться, например, к источнику.

"""

def fibonacci(index):
    if index ==1:
        return 0
    elif index==2:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)

if __name__ == '__main__':
    print(fibonacci(10))