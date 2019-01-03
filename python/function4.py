def add_10(value):
    """value에 10을 더한 값을 돌려주는 함수"""
    if value < 10:
        result = 10
    else:
        result = value + 10
    return result

n = add_10(5)
print(n)
n = add_10(42)
print(n) 