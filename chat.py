#print prime numbers 1 to 100

import math
for i in range(2,101):
    for j in range (2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)
        


