num_list = [10, 20, 30, 40, 50]
num = 0

for i in range(len(num_list)):
    num += num_list[i]

print(f'합계: {num}')
print(f'평균: {num/len(num_list):.1f}')
