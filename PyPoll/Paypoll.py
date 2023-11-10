import os
#see current directory
print(os.getcwd())
#change directory to read election data csv file (Specify path according to your file location)
os.chdir(r"C:\\Users\\gaupa\\Desktop\\Python Project\\Starter_Code\\Pypoll\\Resources")
print(os.getcwd())
import csv


#define variables
Total_Votes= 0
Candidate_List = []
Charles_Casper_Stockham_Count = 0
Diana_Degette_Count = 0
Raymon_Anthony_Doane_Count = 0


#Open csv file 
with open("election_data.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    
    #Get total votes
    for row in csv_reader:
      Total_Votes +=1
      
      
      #List of candidate
      candidate = row["Candidate"]
      if candidate not in Candidate_List:
         Candidate_List.append(candidate)
         print(Candidate_List)

       #Get Individual candidate vote counts and print them
      if row["Candidate"]== "Charles Casper Stockham":
         Charles_Casper_Stockham_Count +=1
      if row["Candidate"]== "Diana DeGette":
         Diana_Degette_Count +=1
      if row["Candidate"]== "Raymon Anthony Doane":
         Raymon_Anthony_Doane_Count +=1
    print (Charles_Casper_Stockham_Count)
    print(Diana_Degette_Count)
    print(Raymon_Anthony_Doane_Count)

    #Get percent of toatal votes for individual candidate

    Charles_Casper_Stockham_Percent = Charles_Casper_Stockham_Count/Total_Votes *100
    Diana_Degette_Percent = Diana_Degette_Count/Total_Votes *100
    Raymon_Anthony_Doane_Percent = Raymon_Anthony_Doane_Count/ Total_Votes *100
    print(Charles_Casper_Stockham_Percent)
    print(Diana_Degette_Percent)
    print (Raymon_Anthony_Doane_Percent)

    #Create dictionary to list cadidate and votes for individual candidate
    global_list = {"Charles Casper Stockham":Charles_Casper_Stockham_Count, "Diana Degette":Diana_Degette_Count, "Raymon Anthony doane":Raymon_Anthony_Doane_Count}
    percent_list = {"Charles Casper Stockham":Charles_Casper_Stockham_Percent, "Diana Degette":Diana_Degette_Percent, "Raymon Anthony doane":Raymon_Anthony_Doane_Percent }
    print(global_list)
    #Find winner based on max votes from created dictionary
    winner = max(global_list, key= global_list.get)
    print(winner)

    #Create output text file and print relevent information
    file = open ("pypoll_output.txt", "w")
    file.write(" Election Results\n")
    file.write ("-----------------------------------\n")
    file.write("Total Votes:" + str(Total_Votes))
    file.write("\n-----------------------------------\n")
    file.write(str(global_list))
    file.write("\n" + str(percent_list))
    file.write("\n------------------------------------\n")
    file.write("Winner:" + str(winner))



         
         


      