def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursion(num - 1)

def factorial_repeat(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


nums = [5, 7]

for num in nums:
    print(f"{num}! (재귀) = {factorial_recursion(num)}")
    print(f"{num}! (반복) = {factorial_repeat(num)}")
