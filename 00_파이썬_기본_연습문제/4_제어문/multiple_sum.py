num_list = []
sum = 0

for i in range(1,101):
    if(i%3 == 0):
        num_list.append(i)
        sum += i 

print(f'1부터 100까지 3의 배수: {num_list}')
print(f'3의 배수의 합: {sum}')
print(f'3의 배수의 개수: {len(num_list)}')