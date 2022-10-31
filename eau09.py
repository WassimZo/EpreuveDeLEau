import sys

def constructResult(min, max) :
   global result
   result = "" 
   for nbr in range(min, max) :
      result = result + str(nbr)+ ' '

if len(sys.argv) != 3 :
   print("error")
   sys.exit()

try : 
   first = int(sys.argv[1])
   second = int(int(sys.argv[2]))
   if first >= second :
      constructResult(second, first)
   else : 
      constructResult(first, second)

   print(result)

except ValueError :
   print("error")
   sys.exit()  

