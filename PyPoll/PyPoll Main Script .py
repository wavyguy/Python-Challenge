#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv
from pathlib import Path


# In[3]:


csvpath = os.path.join("..", "Resources", "electiondata.csv" )


# In[4]:


#Set Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#Open Data into CSV Reader and Skip First Row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Place Count for Unique Voter ID's
    for row in csvreader:
        total_votes +=1
        
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1     


# In[5]:


#Make Dictionary Out of List
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]


# In[6]:


#Use Dictionary to Zip List Together & Choose Winner 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


# In[7]:


#Analysis
khan_percent = ((khan_votes)/(total_votes)) *100
correy_percent = ((correy_votes)/(total_votes)) * 100
li_percent = ((li_votes)/(total_votes))* 100
otooley_percent = ((otooley_votes)/(total_votes)) * 100


# In[8]:


#Print Summary Table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")


# In[9]:


#Actions to Place Onto Text File

output = Path("..", "PyPoll", "election_output.txt")

with open(output,"w") as file:


    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")


# In[ ]:




