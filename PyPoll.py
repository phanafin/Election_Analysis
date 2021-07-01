# The data we need to retrieve.
# Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
election_data = open(file_to_load, 'r')
total_votes = 0
candidate_options =[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# To do: read and analyze the data here.
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        candidate_name = row[2]
# Print the candidate name from each row
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
print(candidate_votes)
#3. The percentage of votes each candidate won.
for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
print(winning_candidate_summary)

#2. A complete list of candidates who received votes.  print(candidate_options)
#1. The total number of votes cast.
print(total_votes)

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




#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.
