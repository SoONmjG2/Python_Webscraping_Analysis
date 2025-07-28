import csv

grades = [
    ["김철수", 85],
    ["이영희", 92],
    ["박민수", 78],
    ["최수진", 95]
]

with open("grades.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "점수"]) 
    writer.writerows(grades)

print("학생 성적이 grades.csv에 저장되었습니다.\n")

sum= 0
count = 0

print("성적 분석 결과:")
with open("grades.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    for row in reader:
        name, score = row[0], int(row[1])
        print(f"{name}: {score}점")
        sum += score
        count += 1

average = sum / count
print(f"전체 평균: {average:.1f}점")
