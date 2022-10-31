import sys

if len(sys.argv) != 2 :
   print("error")
   sys.exit()

try :
   nbr = int(sys.argv[1])
   print("error")
   sys.exit()
except ValueError :
   words = str(sys.argv[1]).replace('\n', ' ')
   words = words.replace('\t', ' ')
   words = words.split(' ')
   result = ""

   for word in words :
      result = result + word[0].upper()
      result = result + word[1:]
      result = result + ' '

   print(result)