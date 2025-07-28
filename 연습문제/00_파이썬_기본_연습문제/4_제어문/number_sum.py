sum = 0

while(1):
    
    num = int(input('숫자를 입력하세요 (0을 입력하면 종료): '))

    if num == 0:
        print(f'입력된 숫자들의 합: {sum}')
        break

    sum +=num