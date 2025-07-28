import math

dot1 = (0, 0)
dot2 = (3, 4)

print(f'점1 : {dot1}')
print(f'점2 : {dot2}')
print(f'두 점 사이의 거리: {math.sqrt((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2)}')


