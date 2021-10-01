a = []
for i in range(1,100+1):
    a.append(i)	
#print("1)",a)

for i in range(len(a)):             
    digit_1 = a[i] % 10  
    digit_2 = a[i] // 10 	
    if digit_1 == 1 and digit_2 != 1:	         
        print(a[i],"percent") 
    elif (digit_1 == 2 or digit_1 == 3 or digit_1 == 4) and digit_2 != 1:
        print(a[i],"percent_A")
    else:
        print(a[i],"percent_OFF")
        