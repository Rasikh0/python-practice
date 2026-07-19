def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num): 
  last_digit = num % 10
  if last_digit >= 5:
    return num + (10 - last_digit)
  else:
    return num - last_digit
  
