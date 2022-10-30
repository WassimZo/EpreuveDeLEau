import sys

if len(sys.argv) < 2 : 
   print("error")
   sys.exit()

sys.argv.pop(0)

index = len(sys.argv)-1

while index >= 0 :
   print(sys.argv[index])
   index = index-1