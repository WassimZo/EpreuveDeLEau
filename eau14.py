import sys 

def sortStringArray(table) :
   for indexDown in range(len(table), 1, -1) : 
      for indexUp in range(0, indexDown-1, +1) :
         if min(table[indexUp+1], table[indexUp]) == table[indexUp+1] : 
            k = table[indexUp+1]
            table[indexUp+1] = table[indexUp]
            table[indexUp] = k

   return table

args = sys.argv[1:]

if len(args) == 0 : 
   print("error")
   sys.exit()

args = sortStringArray(args)
result = ""

for word in args : 
   result = result + word + " "

print(result)