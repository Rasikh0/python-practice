def make_bricks(small, big, goal):
  small = small*1 
  big = big*5
  if small + big >= goal and goal % 5 <=small:
    return True
  return False
