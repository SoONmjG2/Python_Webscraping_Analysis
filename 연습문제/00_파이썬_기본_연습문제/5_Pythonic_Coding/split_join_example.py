text = "Python is awesome programming language"


words = text.split()


print(f"원본 문자열: {text}")

print(f"분리된 단어들: {words}")

hyphen_joined = "-".join(words)
print(f"하이픈으로 연결: {hyphen_joined}")

upper_joined = " ".join([word.upper() for word in words])
print(f"대문자로 변환 후 공백으로 연결: {upper_joined}")