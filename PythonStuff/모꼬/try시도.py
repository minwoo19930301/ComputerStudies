a=''
try:
	for i in range(1000):
		str(i)-str(i)
except TypeError as i:
            a=i
else:
            print(a)        
