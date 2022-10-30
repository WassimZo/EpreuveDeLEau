result = ""
for left in range(0, 100) :
   for right in range(0, 100):
      if left < right :
         if left < 10 :
            leftStr = "0"+str(left)
         else :
            leftStr = str(left) 
         if right < 10 :
            rightStr = "0"+str(right)
         else :
            rightStr = str(right)

         result = result+leftStr+" "+rightStr+", "

result = result[:-2]
print(result)
