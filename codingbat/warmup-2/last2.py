def last2(str):
   
   count = 0
   substring = str[-2:]
   
   for i in range(len(str) - 2):
     if str[i:i+2] == substring:
       count += 1
   return count
