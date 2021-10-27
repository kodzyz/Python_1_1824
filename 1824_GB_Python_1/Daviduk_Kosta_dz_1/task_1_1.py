per= int(input('Enter sec:  '))
#per = 604800

sec = per % 60
s = per - sec
min_com = s / 60
min = min_com % 60
m = min_com - min
hour_com = m / 60
hour = hour_com % 24
h = hour_com - hour
day_com = h / 24
day = day_com % 30  

if day != 0:
    print("%d Day" %(day), end=' ')
if hour != 0:
    print("%d Hr" %(hour), end=' ')	
if min != 0:
    print("%d Min" %(min), end=' ')
if sec != 0:
    print("%d Sec" %(sec), end=' ')    


