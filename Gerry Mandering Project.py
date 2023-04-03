"""
    Description of program: Project 6 - Gerrymandering
    Filename: Project 5 - Muskan Fatima
    Author: Muskan Fatima
    Date: 16th February 2023
    Course: PROG 1352
    Assignment: Project 6
    Collaborators: -
    Internet Source: Stack Overflow for reference
"""

import csv
import itertools
results = {}
#reading the file
with open("1976-2020votes.txt", 'r') as f:
     for line in f:
          #splitting each line with the file where there is a comma
          data = line.strip().split(",")      
          #storing the first content of the file in variable year  
          year = data[0]         
          #storing the second content of the file in variable state
          state = data[1]         
          #if the year is not present in the dictionary
          if year not in results:      
        #create a dictionary in the main dictionary with that year as a key       
               results[year] = {}       
          #if a state is not present in the dictionary of each year's dictionary, make a dictionary  
          if state not in results[year]:         
           #the contents of the nested dictionay should be a list    
               results[year][state] = []         
           #add contents in the tuple for the length of each sentence, skip three 
               for i in range(2, len(data), 3):             
                    tup = (data[i], int(data[i+1]), int(data[i+2]))   
            #add that tuple in the list          
                    results[year][state].append(tup)
def report_efficiency_gap(year, state):
        half_vote=0
        dem_waste=0
        rep_waste=0
        num_districts=0
        gap=0
        favor=0
        elections=[]


        elections=list(itertools.chain(*(results[str(year)][str(state)])))
        for i in range (0,(len(elections)), 3): 
            num_districts+=1
        temp_list=[x for x in elections if isinstance(x, int)]
        dem_votes=[temp_list[x] for x in range (0, len(temp_list)) if x%2==0]
        rep_votes=[temp_list[x] for x in range (0, len(temp_list)) if x%2!=0]
        total_votes=int(sum(dem_votes))+int(sum(rep_votes))


  #calculating the wasted votes
        for i in range (0,(len(dem_votes))):
            total=dem_votes[i]+rep_votes[i]
            half_vote=total/2
            if dem_votes[i]>half_vote:
                rep_waste+=rep_votes[i]
                dem_waste+= dem_votes[i]-half_vote
            elif rep_votes[i]>half_vote:
                dem_waste+=dem_votes[i]
                rep_waste+= rep_votes[i]-half_vote
            half_vote=0
            total=0

# #comparing who has the favor in the state
        if dem_waste<rep_waste:
            favor="Republicans"
        else:
            favor="Democrats"
        gap=(rep_waste-dem_waste)/(total_votes)*100
        gap=round(gap,2)
        #printing the results out
        print(f"{num_districts} districts.")
        print(f"Wasted Democratic votes: {dem_waste}")
        print(f"Wasted Republican votes: {rep_waste}")
        print(f"Efficiency gap: {gap}%, in favor of {favor}.")


user_input_year = ''
user_input_state = ''
user_input=''


#main part of the program
while user_input != 'no':
    print("This program evaluates districting fairness for US House elections from 1976-2020.")
    user_input_year=int(input("What election year would you like to evaluate? "))
    user_input_state = input("What state would you like to evaluate? ").upper()
    while user_input_year %2 !=0 or user_input_year>2020 or user_input_year<1976:
         user_input_year=int(input("What election year would you like to evaluate? Even years only and years less than 2020 or greater than 1976: "))
    
    while user_input_state not in results[user_input_year].keys():
        user_input_state = input("Wrong state. Please spell correctly:  ").upper()
    report_efficiency_gap(user_input_year, user_input_state)
    user_input=input("Would you like to continue? ")

