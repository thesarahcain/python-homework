import os
import csv
input_data = os.path.join("Resources", "election_data.csv")
total_votes = 0
out_put_folder = "Analysis"
output_file = os.path.join(out_put_folder, "Final_poll_analysis.txt")


with open(input_data, "r") as file:
    print("Election Results")
    print("-" * 30)
    election_data = list(csv.reader(file))
    total_votes = len(election_data) -1 
    print(f"Total Vote:{total_votes}")
    print("-" * 30)

    candidate_votes = {}
    for row in election_data:

        #checkin the duplicates
        voter_id = row[0]
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
           candidate_votes[candidate] = 1
    
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    
    if votes ==1:
        pass
    else:
        print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-" * 30)
election_winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {election_winner}")
print("-" * 30)

# writing in the text file:
with open(output_file, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-" * 30 + "\n")
    output_file.write(f"Total Vote:{total_votes}\n")
    output_file.write("-" * 30 + "\n")   
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        
        if votes ==1:
            pass
        else:
            output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-" * 30 + "\n")
    election_winner = max(candidate_votes, key=candidate_votes.get)
    output_file.write(f"Winner: {election_winner}\n")
    output_file.write("-" * 30)

print(f"Analysis are written to {output_file} under Analysis folder")
    