# The data we need to retrieve.
# Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
election_data = open(file_to_load, 'r')
# Open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file.

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
    
# Close the file
outfile.close()

  
    # Close the file.
election_data.close()

#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.
