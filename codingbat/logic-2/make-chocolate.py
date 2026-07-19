def make_chocolate(small, big, goal):
  big_used = min(big, goal // 5)
  remainder = goal - big_used * 5
  if small >= remainder:
    return remainder
  else:
    return -1
  
