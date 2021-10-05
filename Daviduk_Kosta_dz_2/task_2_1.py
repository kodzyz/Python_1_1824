#2.1 Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

a = 15 * 3
print(type(a)) #<class 'int'>
b = 15 / 3
print(type(b)) #<class 'float'>
print(isinstance(b, float)) #True
c = 15 // 2
print(type(c)) #<class 'int'>
d = 15 ** 2
print(type(d)) #<class 'int'>
