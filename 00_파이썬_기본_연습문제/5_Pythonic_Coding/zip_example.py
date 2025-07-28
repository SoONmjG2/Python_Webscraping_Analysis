students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

grades = dict(zip(students, scores))

print('학생과 점수 매칭:')
for name, score in grades.items():
    print(f'{name}: {score}점')

print(f'점수별 학생 딕셔너리: {grades}')
