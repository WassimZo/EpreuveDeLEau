import sys 

def createTable(args) :
   table = []
   for nbr in args :
      table.append(int(nbr))
   return table 

def bubbleSort(table) : 
   for indexDown in range(len(table), 1, -1) : 
      for indexUp in range(0, indexDown-1, +1) :
         if table[indexUp+1] < table[indexUp] : 
            k = table[indexUp+1]
            table[indexUp+1] = table[indexUp]
            table[indexUp] = k

   return table

try : 
	if len(sys.argv)  < 2 : 
	   print("error")
	   sys.exit()


	table = createTable(sys.argv[1:])
	table = bubbleSort(table)
	result = ""
	for nbr in table :
	   result = result + str(nbr) + " "

	print(result)

except ValueError : 
   print("error")
   sys.exit()