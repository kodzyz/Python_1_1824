# task_1.py
# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield

# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def odd_nums(n):
    for num_odd in range(1, n + 1, 2):
        yield num_odd


odd_to_15 = odd_nums(15)
# for i in odd_to_15:
#     print(i, end=' ')

print(next(odd_to_15)) # 1...
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
print(next(odd_to_15)) # ...15

next(odd_to_15)
#тут - StopIteration

