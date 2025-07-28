num_list =  [15, 3, 27, 8, 19, 12, 31]


max_num = num_list[0]
min_num = num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

second_max = 0
for num in num_list:
    if num != max_num:
        if  num > second_max:
            second_max = num

# 결과 출력
print(f'숫자 목록: {num_list}')
print(f'최댓값: {max_num}')
print(f'최솟값: {min_num}')
print(f'두 번째로 큰 값: {second_max}')