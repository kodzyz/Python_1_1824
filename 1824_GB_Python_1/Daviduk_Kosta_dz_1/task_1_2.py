odd_cube_list = [] 
div_sev = []
div_sev_two = []
sum_n = 0
suma = 0
suma_two = 0
# функция проверки что сумма цифр числа /7 
def sum_dig_div7(x):    
    idx = x
    sum_digit = 0    
    digit = 0    
    while idx > 0:
		   digit = idx % 10	  #извлечь последнюю цифру числа 
		   sum_digit += digit # сумма цифр числа 
		   idx //= 10     #Избавиться от последней цифр числа
    if sum_digit % 7 == 0:    #которые делятся нацело на 7       
         return True          #правда

#2
# список 1, состоящий из кубов нечётных чисел от 1 до 1000
for i in range(1,1000,2):
    odd_cube_list.append(i**3)
print("List1_for_task_2 ",odd_cube_list)

#создаю список 2,
#состоящий из чисел списка 1, 
#сумма цифр которых делится нацело на 7 
for i in odd_cube_list:    
    if sum_dig_div7(i): # функция
        div_sev.append(i)  
print("List2_for_task_2a ",div_sev) 
 
#2.a 
# Вычислить сумму чисел
for i in div_sev:    
    sum_n += i
print("Sum_task_2a ",sum_n)

#2b.1 
# к каждому элементу списка 1 добавить 17
for i in range(len(odd_cube_list)):
    odd_cube_list[i] += 17    
print("List1_change_+17",odd_cube_list)

#2b.2
# вычислить сумму тех чисел из этого списка, 
#сумма цифр которых делится нацело на 7. 

#for i in odd_cube_list:    
 #   if sum_dig_div7(i):
  #      div_sev_two.append(i) # новый список 
  #      suma += i
#print("List4_Sum_digits_List3_div_7 =",div_sev_two)
#print("_Sum_digits_List3_div_7 =",suma)

#2с решилась по идее в 2b если вычислять только сумму
# а вот изменить список 1 чтоб в нем остался только
#список из чисел
#сумма цифр которых делится нацело на 7 
#получилась только с циком while

#2с
i = 0
while i < len(odd_cube_list ):
    if not sum_dig_div7(odd_cube_list [i]):
        del odd_cube_list [i]
    else:        	    
        i += 1
print("List1_change_task_2c", odd_cube_list )

for i in odd_cube_list:    
    suma_two += i
print("Sum_task_2c ",suma_two)