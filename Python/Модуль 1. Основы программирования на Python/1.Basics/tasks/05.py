"""
Python часто используют для решения математических задач, одна из них — вычисление суммы ряда. Напишите программу,
 которая будет вычислять и выводить на экран сумму квадратов натуральных чисел до N, где N — натуральное число (N>1),
 подаваемое на вход программы.

1+2^2+3^2+...+N^2

"""
# We need to print the sum of squares
if __name__ == '__main__':
    N = int(input())
    sum_of_numbers = 0
    for i in range(1, N + 1):  # If we just do here in range (N) then we would get error because of 0 indexing
        sum_of_numbers += i ** 2  # to square use 2 and not i**i
    print(sum_of_numbers)
