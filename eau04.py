import sys

def primeTest(test) :
   if test == 0 or test == 1 : 
      return False
   for nbr in range(2, test) :
      if test % nbr == 0 :
         return False 

   return True

if len(sys.argv) != 2 :
	print(-1)
	sys.exit()
 
try :
   argNbr = int(sys.argv[1])
except ValueError:
   print(-1)
   sys.exit()

nextPrime = 0

while nextPrime == 0 :
   if primeTest(argNbr+1) :
      nextPrime = argNbr+1
   else :
      argNbr = argNbr+1

   


print(nextPrime)