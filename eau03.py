import sys 

fibo = [0, 1, 1, 2]
   
if len(sys.argv) != 2 :
   print("erreur")
   sys.exit()

try : 
   index = int(sys.argv[1])
except ValueError:
   print("erreur")
   sys.exit()

if index > 3 : 
   for nbr in range (4, index+1):
      fibo.append(fibo[nbr-2]+fibo[nbr-1])

   result = fibo.pop()
else : 
   result = fibo[index]



print(result)