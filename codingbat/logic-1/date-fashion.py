def date_fashion(you, date):
  no = 0
  maybe = 1
  yes = 2
  
  if you <= 2 or date <= 2:
    return no
  if you >= 8 or date >= 8:
    return yes
  return maybe
