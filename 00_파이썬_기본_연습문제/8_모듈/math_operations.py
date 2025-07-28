import math

def math_calculate_r(num):
    print(f'원의 넓이: {num*num*math.pi:.2f}')

def math_calculate_rect(num1,num2):
    print(f'직사각형 넓이: {num1*num2}')

def math_calculate_fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f'팩토리얼 {num}! = {result}')

def math_calculate_max(num1,num2):
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    print(f"최대공약수({num1}, {num2}) = {a}")