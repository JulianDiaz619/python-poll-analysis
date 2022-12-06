import csv
import os

fileload = os.path.join("Resources","election_results.csv")
filesave = os.path.join("analysis","election_results.txt")

counties = []
county_votes = {}
total_votes_counties = 0

total_votes_candidates = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count_candidate = 0
winning_percentage_candidate = 0

winning_county = ""
winning_count_county = 0
winning_percentage_county = 0

with open(fileload) as dataset:
    data = csv.reader(dataset)
    headers = next(data)
    for row in data:
        total_votes_counties += 1
        county_name = row[1]
        if county_name not in counties:
            counties.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

with open(fileload) as dataset:
    data = csv.reader(dataset)
    headers = next(data)
    for row in data:
        total_votes_candidates += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

print(county_votes)
print(candidate_votes)

with open(filesave, "w") as txt:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_counties:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt.write(election_results)
    county_header = (f"County Votes:\n")
    print(county_header)
    txt.write(county_header)
    

    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes_counties) * 100
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt.write(county_results)

        if (votes > winning_count_county) and (vote_percentage > winning_percentage_county):
         winning_count_county = votes
         winning_county = county_name
         winning_percentage_county = vote_percentage
    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
    
    print(winning_county_summary)
    txt.write(winning_county_summary)

    for candidate_name in candidate_votes:
        votes_candidates = candidate_votes[candidate_name]
        vote_percentage_candidates = float(votes_candidates) / float(total_votes_candidates) * 100
        candidate_results = (f"\n{candidate_name}: {vote_percentage_candidates:.1f}% ({votes_candidates:,})\n")
        print(candidate_results)
        txt.write(candidate_results)

        if (votes_candidates > winning_count_candidate) and (vote_percentage_candidates > winning_percentage_candidate):
         winning_count_candidate = votes_candidates
         winning_candidate = candidate_name
         winning_percentage_candidate = vote_percentage_candidates
    winning_candidate_summary = (
    f"\n-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count_candidate:,}\n"
    f"Winning Percentage: {winning_percentage_candidate:.1f}%\n"
    f"-------------------------\n")
    
    print(winning_candidate_summary)
    txt.write(winning_candidate_summary)


    
    
  


        
        


