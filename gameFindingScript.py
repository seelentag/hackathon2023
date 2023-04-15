
# TTRPG Game Finding Script
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon

import gameFindingScriptHelperFunctions as gf


# Poking through initial CSV file and cleaning the data for our purposes

filename = "groupfinder.csv"
f = open(filename, "r")
data = f.readlines()
f.close()

users = {}

cleanedData = []

for i in range(6, len(data)):
   cleanedData += data[i].split(",")

for i in range(len(cleanedData)):
   cleanedData[i] = cleanedData[i].replace('\"', '')
   cleanedData[i] = cleanedData[i].strip()


# Creating a dictionary of people with inner lists of avaible times and other preferences

for i in range(len(cleanedData)):
    if cleanedData[i] == "Yes":
       username = cleanedData[i+1]
       day = cleanedData[i+2]
       time = cleanedData[i+3]

       time = gf.get_hour_minute(time)

       users[username] = [day, time]

print(users)



# Matching people based on their available times

times = {}

# for user in users:
#     if user in times:
        

    




# Outputing a CSV file with grouped users





