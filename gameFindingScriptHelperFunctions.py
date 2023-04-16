
# TTRPG Game Finding Script Helper Functions
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon

class user:
  def __init__(self, username, time):
    self.username = username
    self.time = time

class time_group:
  def __init__(self, time):
    self.time = time
    self.people = []
    self.length = 0



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


