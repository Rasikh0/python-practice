def alarm_clock(day, vacation):
  weekday = day in range(1,6)
  if not vacation:
    return "7:00" if weekday else "10:00"
  return "10:00" if weekday else "off"
