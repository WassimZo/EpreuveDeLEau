import sys
import math

def createTable(args) :
   table = []
   for nbr in args :
      table.append(int(nbr))
   return table 

try : 
   if len(sys.argv) < 3 : 
      print("error")
      sys.exit()

   table = createTable(sys.argv[1:])
   index = 0
   diffMinAbs = math.inf
   while index < len(table)-1 :
      nxtIndex = index+1
      while nxtIndex < len(table) :
         if abs(table[index] - table[nxtIndex]) < diffMinAbs :
            diffMinAbs = abs(table[index] - table[nxtIndex])
         nxtIndex = nxtIndex+1
      index = index+1

   print(diffMinAbs)

except ValueError:
   print("error")
   sys.exit()
