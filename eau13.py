import sys 

def createTable(args) :
   table = []
   for nbr in args :
      table.append(int(nbr))
   return table 

def selectSort(table) :
   lenght = len(table)
   for index in range(0, lenght-1) :
      minimum = index
      for nxtIndex in range(index+1, lenght) :
         if table[nxtIndex] < table[minimum] :
            minimum = nxtIndex
      if minimum != index :
         k = table[index]
         table[index] = table[minimum]
         table[minimum] = k 

   return table

try : 
	if len(sys.argv)  < 2 : 
	   print("error")
	   sys.exit()


	table = createTable(sys.argv[1:])
	table = selectSort(table)
	result = ""
	for nbr in table :
	   result = result + str(nbr) + " "

	print(result)

except ValueError : 
   print("error")
   sys.exit()