def combo_string(a, b):
  short_string = a if len(a) < len(b) else b
  long_string = a if len(a) > len(b) else b
  return short_string+long_string+short_string
  
