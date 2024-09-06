import math
try:
    x1 = int(input())
    x2 = int(input())
    result = math.sqrt(x1 ** 2 + x2 ** 2)

except Exception as e:
    print("введи число")
    print(f"произошла ошибка {e}")
else:
    print(f"результат:{result}")