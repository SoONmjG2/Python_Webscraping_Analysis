numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squared = [x**2 for x in numbers]


filtered = [x for x in numbers if x > 5]

filtered_squared = [x**2 for x in filtered]

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared}")
print(f"5보다 큰 수들: {filtered}")
print(f"5보다 큰 수들의 제곱: {filtered_squared}")
