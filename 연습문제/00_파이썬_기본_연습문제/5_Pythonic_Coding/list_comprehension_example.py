numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_list = [n for n in numbers if n % 2 == 0]

num_num_list = [n*n for n in num_list]

print(f'원본 리스트: {numbers}')
print(f'짝수들: {num_list}')
print(f'짝수의 제곱: {num_num_list}')