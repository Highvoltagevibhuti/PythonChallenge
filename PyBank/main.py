import os
#see current directory
print(os.getcwd())
#change directory (You could specify path according to your need)
os.chdir(r"C:\\Users\\gaupa\\Desktop\\Python Project\\Starter_Code\\PyBank\\Resources")
print(os.getcwd())
import csv



#define variables
Total_Months = 0
Total_Profit_Loss_Revenue = 0
ChangeInRevenue = 0
FormerRevenue = 0
Change_List_Over_Entire_Period = []


#Open csv file 
with open("budget_data.csv") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    
    #Get total months
    for row in csv_reader:
      print(row)
      Total_Months +=1
      print(Total_Months)

      #Get Total_Profit_Loss_Revenue i.e summation of profit/Losses column from csv file
      Total_Profit_Loss_Revenue += int(row["Profit/Losses"])
      print (Total_Profit_Loss_Revenue)

      #Change in profit/Losses over the entire period and Average of those changes
      #Create a list by using append with for loop to get change over entire period and use that array to find average max and min
      
      changeInRevenue = int(row["Profit/Losses"]) - FormerRevenue
      FormerRevenue = int(row["Profit/Losses"])
      print (changeInRevenue)
      Change_List_Over_Entire_Period.append(changeInRevenue)
      print (Change_List_Over_Entire_Period)
      Average = (sum(Change_List_Over_Entire_Period))/(len(Change_List_Over_Entire_Period))
      print(Average)


      #Greatest Increase in profit
      Greatest_Increase = max(Change_List_Over_Entire_Period)
      print(Greatest_Increase)


      #Greatest Decrease in profit
      Greatest_Decrease = min(Change_List_Over_Entire_Period)
      print(Greatest_Decrease)

      #Create output text file and print relevent information
      file = open ("pybank_output.txt", "w")
      file.write(" Financial Analysis\n")
      file.write ("-----------------------------------\n")
      file.write("Total Months:" + str(Total_Months))
      file.write("\nTotal: $" + str(Total_Profit_Loss_Revenue))
      file.write("\nAverage Change: $" +str(Average))
      file.write("\nGreatest Increase in profits: $" +str(Greatest_Increase))
      file.write("\nGreatest Decrease in profits: $" +str(Greatest_Decrease))
    

    
      





