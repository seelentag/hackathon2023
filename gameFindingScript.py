
# TTRPG Game Finding Script
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon

import gameFindingScriptHelperFunctions as gf

# Poking through initial CSV file and cleaning the data for our purposes

filename = "GroupfinderWIP.csv"
f = open(filename, "r")
data = f.readlines()
f.close()

cleanedData = []

for i in range(6, len(data)):
   cleanedData += data[i].split(",")

for i in range(len(cleanedData)):
   cleanedData[i] = cleanedData[i].replace('\"', '')
   cleanedData[i] = cleanedData[i].strip()


# Creating a dictionary of people with inner lists of avaible times and other preferences

users = []

for i in range(len(cleanedData)):
    if cleanedData[i] == "Yes":
       username = cleanedData[i+1]
       day = cleanedData[i+2]
       time = cleanedData[i+3]

       time = (day + " " + gf.get_hour_minute(time))

       users.append(gf.user(username, time))


# Matching people based on their available times


time_groups = []

for i in range(len(users)):
   if users[i].time not in time_groups:
      time_groups.append(gf.time_group(users[i].time))


users_added = []


for i in range(len(users)):
   for j in range(len(time_groups)):
      if users[i].username not in users_added and users[i].time == time_groups[j].time and time_groups[j].length < 5:
         time_groups[j].people.append(users[i].username)
         time_groups[j].length += 1
         users_added.append(users[i].username)
      elif (users[i].username not in users_added and users[i].time == time_groups[j].time and time_groups[j].length >= 5):
         time_groups.append(gf.time_group(users[i].time))
         users_added.append(users[i].username)
         group_num = len(time_groups) -1
         time_groups[group_num].people.append(users[i].username)
      else:
         pass


finished_cleaning = False
i = 0
while not finished_cleaning:
   print(time_groups[i].time)
   print(time_groups[i].people)
   if time_groups[i].people == []:
      del time_groups[i]
      i -= 1
   i += 1
   if i == len(time_groups)-1:
      finished_cleaning = True
   



# Outputing a txt file with grouped users

groups = ""

for i in range(len(time_groups)):
   groups += "Group " + str(i) + ": " + time_groups[i].time + ":00, " + str(time_groups[i].people) + "\n"

f = open("output.txt", "w")
f.writelines(str(groups))
f.close




