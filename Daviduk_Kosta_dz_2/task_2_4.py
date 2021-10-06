corr_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
nam = []
s = ''
for i in corr_data:
    n = ''
    s = i
    rev = s[::-1] #ьрогИ роткуртснок-ренежни
    for j in rev:
        if j != ' ':
            n += j
        else:
            break
    nam.append(n[::-1]) #'Игорь'
st_n = ' '.join(nam)
n_1, n_2, n_3 = st_n.split(' ')[:3]
phrase = f'{n_1} - инженер-конструктор'
print(phrase)
phrase = f'{n_2.title()} - главный бухгалтер'
print(phrase)
phrase = f'{n_3.title()} - токарь высокого полета'
print(phrase)
# списка получилось два