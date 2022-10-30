import sys

if len(sys.argv) != 2 :
   print("error")
   sys.exit()

try :
   nbr = int(sys.argv[1])
   print("error")
   sys.exit()
except ValueError :
   string = sys.argv[1]
   result = ""
   upper = True
   for char in string :
      if char.isalpha() : 
         if upper : 
            result = result + char.upper()
            upper = False
         else :
            result = result + char
            upper = True
      else : 
         result = result + char

print(result)