import re
from collections import Counter


text = """파이썬은 쉬운 프로그래밍 언어입니다.
파이썬 프로그래밍을 배우기 쉽고, 강력한 언어입니다.
파이썬을 사용하면 다양한 프로그램을 만들 수 있습니다."""


with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(text)


with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

words = re.findall(r'\b[가-힣]+\b', content)

freq = Counter(words)


print("단어 빈도 분석 결과:")
for word, count in freq.most_common():
    print(f"{word}: {count}번")
