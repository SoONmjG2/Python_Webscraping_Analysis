import math

def list_statistics(my_list):
    total = 0
    for num in my_list:
        total += num
    mean = total / len(my_list)

    max_val = my_list[0]
    min_val = my_list[0]
    for num in my_list:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    variance_sum = 0
    for num in my_list:
        variance_sum += (num - mean) ** 2
    std_dev = math.sqrt(variance_sum / (len(my_list)-1))

    return mean, max_val, min_val, std_dev

my_list = [10, 20, 30, 40, 50]

mean, max_val, min_val, std_dev = list_statistics(my_list)

print(f"숫자들: {my_list}")
print(f"평균: {mean}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std_dev:.2f}")