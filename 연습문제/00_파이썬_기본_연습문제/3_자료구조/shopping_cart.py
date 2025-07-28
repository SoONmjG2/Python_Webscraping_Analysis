shopping_cart = {
    '사과': [2, 1000],
    '바나나': [3, 800],
    '오렌지': [1, 1500]
}

total_price = 0

print('쇼핑 카트:')
for item, (qty, price) in shopping_cart.items():
    item_total = qty * price
    total_price += item_total
    print(f'{item}: {qty}개 (개당 {price}원) = {item_total}원')

print(f'총 가격: {total_price}원')