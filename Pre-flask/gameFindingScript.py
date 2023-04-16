
# TTRPG Game Finding Script
# Caden Mcdonough, Joey Dugan

# Written 4/15/23 and 4/16/23 for the Cal Poly Humboldt Hackathon

import gameFindingScriptHelperFunctions as gf

def sort_users_into_groups(filename):

   # Poking through initial CSV file and cleaning the data for our purposes

   cleanedData = gf.open_file_and_clean_data(filename)

   # Creating a dictionary of people with inner lists of avaible times and other preferences

   users_under_18 = []
   users_over_18_under_30 = []
   users_over_30_under_60 = []
   users_over_60 = []

   for i in range(len(cleanedData)):
      if cleanedData[i] == "Yes":
         username = cleanedData[i+1]
         age = int(cleanedData[i+2])
         day = cleanedData[i+3]
         time = cleanedData[i+4]

         time = (day + " " + gf.get_hour_minute(time))

         if age < 18:
            users_under_18.append(gf.user(username, time, age))
         elif age >= 18 and age < 30:
            users_over_18_under_30.append(gf.user(username, time, age))
         elif age >= 30 and age < 60:
            users_over_30_under_60.append(gf.user(username, time, age))
         else:
            users_over_60.append(gf.user(username, time, age))


   # Matching people based on their available times



   time_groups_under_18 = gf.sort_users(users_under_18)
   time_groups_under_30 = gf.sort_users(users_over_18_under_30)
   time_groups_under_60 = gf.sort_users(users_over_30_under_60)
   time_groups_over_60 = gf.sort_users(users_over_60)


   # Outputing a txt file with grouped users

   groups_under_18 = gf.create_group_string(time_groups_under_18)
   groups_under_30 = gf.create_group_string(time_groups_under_30)
   groups_under_60 = gf.create_group_string(time_groups_under_60)
   groups_over_60 = gf.create_group_string(time_groups_over_60)

   groups = gf.concatenate_age_groups(groups_under_18, groups_under_30, groups_under_60, groups_over_60)

   f = open("output.txt", "w")
   f.writelines(str(groups))
   f.close

   return (str(groups))


if __name__ == "__main__":
   filename = "Groupfinderwip.csv"
   sort_users_into_groups(filename)

