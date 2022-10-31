import sys

searched = sys.argv[-1]
searchDomain = sys.argv[1:-1]

index = 0
for word in searchDomain :
   if word == searched :
      print(index)
      sys.exit()
   else : 
      index = index+1
print(-1)