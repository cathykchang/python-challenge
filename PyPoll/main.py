# dependencies
import os
import csv

# locate csv file to open
ref_csv_path = os.path.join('Resources', 'election_data.csv')

# open cvs file as object, specify the variable to hold the contents
with open(ref_csv_path, encoding='utf') as csv_object:
    
    # open object as a text file
    csv_text = csv.reader(csv_object,delimiter=',')
    
    # skip the header row
    csv_header = next(csv_text)

    # set variable container for total votes
    total_votes = 0
  
    # create a dictionary of candidates
    candidates = {}

    # create a list of candidates
    candidates_list = [
        "Charles Casper Stockham",
        "Diana DeGette",
        "Raymon Anthony Doane"]
    
    # declare the candidates list as a key in the candidates dictionary
    candidates["name"] = candidates_list

    # initiate vote count variables for each candidate
    charles_vote_count = 0
    diana_vote_count = 0
    raymon_vote_count = 0

    # initiate for loop
    for row in csv_text:
        
        # count total number of votes (rows)
        total_votes += 1             

        # if the name in column 3 is equal to the candidate, add a vote to their vote count
        if str(row[2]) == "Charles Casper Stockham":
            charles_vote_count += 1
        if str(row[2]) == "Diana DeGette":
             diana_vote_count += 1
        if str(row[2]) == "Raymon Anthony Doane":
             raymon_vote_count += 1

# calculate the % of votes each candidate received
charles_percent = charles_vote_count / total_votes
diana_percent = diana_vote_count / total_votes
raymon_percent = raymon_vote_count / total_votes

# print results
print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(total_votes))
print("-------------------------")
print(f'{candidates["name"][0]}: {charles_percent:.3%} ({charles_vote_count})')
print(f'{candidates["name"][1]}: {diana_percent:.3%} ({diana_vote_count})')
print(f'{candidates["name"][2]}: {raymon_percent:.3%} ({raymon_vote_count})')
print("-------------------------")

# determine winner
if charles_vote_count > diana_vote_count and charles_vote_count > raymon_vote_count:
    winner = candidates["name"][0]
if diana_vote_count > raymon_vote_count and diana_vote_count > raymon_vote_count:
    winner = candidates["name"][1]
if raymon_vote_count > diana_vote_count and raymon_vote_count > charles_vote_count:
    winner = candidates["name"][2]
print('Winner: ' + str(winner))
print("-------------------------")

# specify the folder to write the text file to
analysis_path = os.path.join('analysis', 'analysis.txt')

# open the file using "write" mode, specify the variable to hold the contents
with open(analysis_path, 'w') as analysis_file:

    # print rows in text file
    analysis_file.write("Election Results \n")
    analysis_file.write("------------------------- \n")
    analysis_file.write("Total Votes: %s \n" % (total_votes))
    analysis_file.write("------------------------- \n")
    analysis_file.write(f'{candidates["name"][0]}: {charles_percent:.3%} ({charles_vote_count}) \n')
    analysis_file.write(f'{candidates["name"][1]}: {diana_percent:.3%} ({diana_vote_count}) \n')
    analysis_file.write(f'{candidates["name"][2]}: {raymon_percent:.3%} ({raymon_vote_count}) \n')
    analysis_file.write("------------------------- \n")
    analysis_file.write("Winner: %s \n" % (winner))
    analysis_file.write("-------------------------")