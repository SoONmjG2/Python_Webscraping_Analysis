list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merge_list = sorted(set(list1 + list2))

element = sorted(set(list1) & set(list2))

print(f'리스트1: {list1}')
print(f'리스트2: {list2}')
print(f'병합된 리스트: {merge_list}')
print(f'공통 요소: {element}')