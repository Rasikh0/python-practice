def lone_sum(a, b, c):
  sum = a+b+c
  
  if a == b:
    sum -= a+b
    
  if a == c:
    sum -= a+c
  
  if b == c:
    sum -= b+c
  
  if a == b == c:
    sum = 0
  
  return sum
    
