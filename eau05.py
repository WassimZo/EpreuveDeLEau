import sys

if len(sys.argv) != 3 : 
   print("error")
   sys.exit()

first = sys.argv[1]
second = sys.argv[2]

if first.find(second) != -1 :
   print("true")
else :
   print("false")