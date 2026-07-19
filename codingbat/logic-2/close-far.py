def close_far(a, b, c):
  b_close = abs(b-a) <= 1
  c_close = abs(c-a) <= 1
  b_far = abs(b-a) >= 2 and abs(b-c) >= 2
  c_far = abs(c-a) >= 2 and abs(c-b) >= 2
  return (b_close and c_far) or (c_close and b_far)
