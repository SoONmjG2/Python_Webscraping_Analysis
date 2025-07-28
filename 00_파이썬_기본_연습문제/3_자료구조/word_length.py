word_list = ['cat', 'elephant', 'dog', 'butterfly', 'ant']


long = word_list[0]
short = word_list[0]

for word in word_list:
    if len(word) > len(long):
        long = word
    if len(word) < len(short):
        short = word

print(f"단어 목록: {word_list}")
print(f"가장 긴 단어: {long} ({len(long)}글자)")
print(f"가장 짧은 단어: {short} ({len(short)}글자)")