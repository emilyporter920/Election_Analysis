#Lists
counties=["Arapahoe","Denver","Jackson"]

print(counties[1])

print(counties[-1])

print(len(counties))

print(counties[0:2])

counties.append("El Paso")

counties.insert(2, "El Paso")

counties.remove("El Paso")

print(counties)

#Pop removes a certain index and then returns the removed item in the terminal
counties.pop(3)

print(counties)

counties[2]="El Paso"

print(counties)

#Tuples
counties_tuple=("Arapahoe","Denver","Jefferson")

#Length Function
print(len(counties_tuple))

#Slicing Function
print(counties_tuple[:-1])

#Dictionaries
counties_dict={}

counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438

print(counties_dict)

#Items Function
print(counties_dict.items())

#Keys Function
print(counties_dict.keys())

#Values Function
print(counties_dict.values())

#Get Function
print(counties_dict.get("Arapahoe"))

#Voting Data
voting_data=[]

voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters":432438})

print(voting_data)


"""# How many votes did you get?
# Input will prompt the user to enter an amount
my_votes=int(input("How many votes did you get in the election? "))

# Total votes in the election
# Int() is needed because when someone enters into the input box it is considered a string
# If you wanted to use a floating-point decimal number you would do float ()
total_votes=int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received
percentage_votes=(my_votes/total_votes)*100

# The percentage votes now needs to be changed into a string using str() to use it as a sentence
print("I received " + str(percentage_votes)+"% of the total votes.")

counties=["Arapahoe","Denver","Jefferson"]

if counties[1]=="Denver":
    print(counties[1])"""

"""If else
temperature= int(input("What is the temperature outside? "))
if temperature > 80:
   print("Turn on the AC.")

else:
   print("Open the windows.")"""

"""Else if (elif)
What is the score?

score=int(input("What is your test score? "))

Determine the grade:

if score>= 90:
    print("Your grade is an A.")

elif score >=80:
        print("Your grade is a B.")

elif score >=70:
        print("Your grade is a C.")

elif score >=60:
        print("Your grade is a D.")

else:
    print("Your grade is an F.")"""

counties=["Arapahoe","Denver","Jefferson"]



#If - Else Statement
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")



#If - And Statement
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso are not in the list of counties")



#If - Or Statements
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")



# For Loops
for county in counties:
    print(county)

# Iterate through Lists and Tuples

# i is 0 which is the index number of "Arapahoe" and goes through all of the items are printed
for i in range(len(counties)):
    print(counties[i])



# Iterate through a Dictionary
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

# The values are outputted from these
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))


# Items() gets the key and the value for each dictionary.
# In this case the key is the county name and the value are the registered voters
for county, voters in counties_dict.items():
    print(county, voters)

print(voting_data)

""" To iterate over the list of dictionaries printing the counties in voting data:

for i in range(len(voting_data)):
    print(voting_data[i]['county'])"""

# Value is the number associated in the dictionary
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

""" To retrieve the number of registered voters from each dictionary:
for county_dict in voting_data:
    print(county_dict['registered_voters']"""

for county_dict in voting_data:
    print(county_dict['county'])

""" Original Code:
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")"""

""" New Code Using f-strings 

my_votes=int(input("How many votes did you get in the election? "))
total_votes=int(input("What is the total votes in the election? "))
print(f"I received {my_votes/total_votes * 100}% of the total votes.")"""

counties_dict={"Arapahoe":369237,"Denver":413229,"Jefferson":390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")



"""# Multiline F-Strings
candidate_votes=int(input("How many votes did the candidate get in the election? "))
total_votes=int(input("What is the total number of the votes in the election? "))
message_to_candidate= (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/total_votes * 100}% of the total votes.")

print(message_to_candidate)"""

# Format Floating-Point Decimals (Putting a limit on the decimal points above)
##f'{value:{width},.{precision}}'
### So .2f would be to 2 decimal places and :, is to add a , in the thousands so instead of 23123 it's 23,123

candidate_votes=int(input("How many votes did the candidate get in the election? "))
total_votes=int(input("What is the total number of the votes in the election? "))
message_to_candidate= (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes/total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)



counties_dict={"Arapahoe":369237,"Denver":413229,"Jefferson":390222}

# Skill drill one using the counties_dict
skilldrillone=(
    f"{counties_dict.items()} county has {counties_dict.values():,} registered voters"
)

print(skilldrillone)

# Import the datetime class from the datetime module
import datetime as dt

# Use the now() attribute on the datetime class to get the present time
now=dt.datetime.now

# Print the present time
print("The time right now is ", now)



# Import CSV
import csv

dir(csv)


# Return all functions available on a variable
print(dir({"Arapahoe":422829,"Denver":463353,"Jefferson":432438}))

print(dir(str))

# Find the dir for the data types and structures
import random
"""import numpy"""

print(dir(int))
print(dir(float))
print(dir(bool))
print(dir(list))
print(dir(tuple))
print(dir(dict))
"""print(dir(datetime))"""

# Direct Path to the File
# Assign a variable for the file to load and the path
file_to_load='Resources/election_results.csv'

# Open the election results and read the file.
election_data=open(file_to_load,'r')

# Perform analysis
# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)


import os
import csv

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file
file_to_save=os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")
    # Write three counties to the file.
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")

