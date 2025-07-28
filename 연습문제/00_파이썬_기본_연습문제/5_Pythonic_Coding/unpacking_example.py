point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

lst = [1, 2, 3]
a, b, c = lst
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def sum_args(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_args(10, 20, 30)}")


def print_info(**kwargs):
    info_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    print(f"키워드 인수들: {info_str}")

print_info(name="김철수", age=25, city="서울")