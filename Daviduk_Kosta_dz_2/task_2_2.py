#Необходимо его обработать — обособить каждое целое число кавычками
# и дополнить нулём до двух целочисленных разрядов:

a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
l = len(a)
i = 0
while i < l:
    s = ''
    s = a[i]
    if '0' <= a[i] <= '9' or s[0] == '+':
        if s[0] == '+'and int(s) < 10:
            a[i] = '+' + '0' + s[1:]
        elif int(s) > 10:
            a[i] = s
        while 1:
            a.insert(i, '  ')
            a.insert(i+2, '  ')
            l = len(a)
            i += 2
            break

    i += 1
print(a)








