import sys 

fibo = [0, 1, 1, 2]
   
if len(sys.argv) != 2 :
   print(-1)
   sys.exit()

try : 
   index = int(sys.argv[1])
except ValueError:
   print(-1)
   sys.exit()

if index > 3 : 
   for nbr in range (4, index+1):
      fibo.append(fibo[nbr-2]+fibo[nbr-1])

   result = fibo.pop()
elif index < 0 : 
   result = -1
else : 
   result = fibo[index]


print(result)