
# TTRPG Game Finding Script Helper Functions
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon






def get_hour_minute(time):
    index = 0
    for i in range(len(time)):
      if time[i] == ":":
        index = i
    hour = time[:index]
    minute = time[index+1:]
    
    return [hour, minute]


def sanitize_user_time(users):
    for user in users:
       if user[1] not in []
       