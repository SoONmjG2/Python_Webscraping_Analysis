import datetime
import random

now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

formatted_date = now.strftime("%Y년 %m월 %d일 %A")
print(f"포맷된 날짜: {formatted_date}")

random_int = random.randint(1, 10)
print(f"임의의 숫자: {random_int}")

random_float = round(random.uniform(1.0, 10.0), 2)
print(f"임의의 실수: {random_float}")

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
random_choice = random.choice(fruits)
print(f"임의의 리스트 요소: {random_choice}")


shuffled_list = fruits[:] 
random.shuffle(shuffled_list)
print(f"섞인 리스트: {shuffled_list}")
