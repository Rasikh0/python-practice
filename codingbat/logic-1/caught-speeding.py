def caught_speeding(speed, is_birthday):
  no_ticket = 0
  small_ticket = 1
  big_ticket = 2
  
  if is_birthday:
    speed -= 5
    
  if speed <= 60:
    return no_ticket
  if speed >= 61 and speed <= 80:
    return small_ticket
  if speed >= 81:
    return big_ticket
