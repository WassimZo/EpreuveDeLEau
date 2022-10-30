result = ""

for a in range(0,10) : 
   for b in range (0,10) :
      for c in range (0,10) :
         if c > b and b > a :
           result = result + str(a)+str(b)+str(c) + ", " 

result = result[:-2]
print(result)