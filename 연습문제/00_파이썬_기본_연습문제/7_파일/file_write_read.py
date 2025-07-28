text = """안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다"""

print(f"파일에 저장할 내용:\n{text}")

with open("example.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\n파일에서 읽어온 내용:")
with open("example.txt", "r", encoding="utf-8") as f:
    print(f.read())