add = input('이메일 주소를 입력하세요:')

lis = add.split('@')
print(f'사용자명: {lis[0]}')
print(f'도메인: {lis[1]}')