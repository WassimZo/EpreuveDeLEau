import sys

if len(sys.argv) != 2 :
   print("error")
   sys.exit()

try : 
   nbr = int(sys.argv[1])
   print("true")
except ValueError :
   print("false")
   sys.exit()
