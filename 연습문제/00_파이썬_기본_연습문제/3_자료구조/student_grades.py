grade = {'김철수':85,'이영희': 92,'박민수': 78,'최수진': 95}
grades = 0


for name, score in grade.items():
    grades += score
    print(f'{name}: {score}점')

print(f'평균 점수: {grades/len(grade):.1f}점')
