# Modules
import os
import csv

# Prompt user for title lookup
book = input("What title are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "comic_books.csv")

# Set variable to check if we found the video
found = False
similars = []

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == book:
            print(row[0] + " was published by " + row[8] + " in " + row[9])

            # Set variable to confirm we have found the video
            found = True
        else:
            title = row[0].split()
            if book in title or book in row[0]:
                similars.append(row[0])


    # If the book is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
        if len(similars) > 0:
            print("Would you be interested in any of these similar titles?")
            for match in similars:
                print(match)
        
