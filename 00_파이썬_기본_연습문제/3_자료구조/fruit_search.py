fruit_list = ['사과', '바나나', '오렌지', '포도', '딸기']
find_fruit = input('찾을 과일을 입력하세요:')

for i in range(len(fruit_list)):
    if(find_fruit == fruit_list[i]):
        print(f"'{find_fruit}'가 목록에 있습니다!")