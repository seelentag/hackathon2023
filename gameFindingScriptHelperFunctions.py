
# TTRPG Game Finding Script Helper Functions
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon






def get_hour_minute(time):
    index = 0
    for i in range(len(time)):
      if time[i] == ":":
        index = i
    hour = int(time[:index])
    minute = time[index+1:]
    
    if minute != "00":
       hour += 1
       hour = hour%24
       minute = "00"
    
    return str(hour)
