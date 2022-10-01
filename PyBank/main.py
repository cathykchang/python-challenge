# dependencies
import os
import csv

# locate csv file to open
csv_path = os.path.join('Resources','budget_data.csv')

# open csv file as an object, specify the variable to hold the contents
with open(csv_path, encoding='utf') as csv_object:

    # open object as a text file
    csv_text = csv.reader(csv_object,delimiter=',')
    
    # skip the header row
    csv_header = next(csv_text)

    # set variable container for total months
    total_months = 0

    # set variable container for total value
    total_value = 0
    
    # set a variable counter for the prior month row
    prior_month = 0

    # set a variable counter for the current month row
    row_count = 0

    # create a list of changes (current month - prior month)
    list_of_changes = []
    
    # create a list saving the period/date and the amount of the biggest positive change within the loop
    max_change = ["",0]
    
    # create a list saving the period/date and the amount of the biggest negative change within the loop
    min_change = ["",0]
    
    # set a variable for the final biggest positive change
    final_inc = 0
    
    # set a variable for the final biggest negative change
    final_dec = 0

    # initiate for loop
    for row in csv_text:
        
        # count what row I'm on
        row_count += 1
        
        # count total months
        total_months += 1
        
        # count total value in the 2nd column
        total_value += int(row[1])
        
        # the 1st month will have no change b/c there is no prior month to compare to
        # so start with
        # if row count is not equal to the first row then
        if row_count != 1:
            
            # calculate the change between current month and prior month
            change = int(row[1]) - prior_month
            
            # add the change to the list of changes
            list_of_changes.append(change) 
            
            # if the monthly change is greater than the biggest positive change then            
            if change > max_change[1]:
                
                # the final biggest positive change value replaces the monthly change value
                final_inc = change
                
                # assign max change date and volume to the current row 
                max_change = [row[0], int(row[1])]
                
            # if the monthly change is less than the biggest negative change then    
            if change < final_dec:
                
                # the final biggest negative change value replaces the monthly change value
                final_dec = change
                
                # assign min change date and volume to the current row
                min_change = [row[0], int(row[1])]                
              
        # set a temporary variable to hold prior month count from one loop to the next loop
        # aka row_count - 1
        prior_month = int(row[1])
        
# calculate average change of entire list
average_change = sum(list_of_changes) / len(list_of_changes)
   
# print analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_value))
print("Average Change: $"+ format(average_change, '.2f'))
print("Greatest Increase in Profits: " + str(max_change[0]) + " ($" + str(final_inc) + ")")
print("Greatest Decrease in Profits: " + str(min_change[0]) + " ($" + str(final_dec) + ")")

# format average_change for printing in text file
text_ave = format(average_change, '.2f')

# specify the folder to write the text file to
analysis_path = os.path.join('analysis', 'analysis.txt')

# open the file using "write" mode, specify the variable to hold the contents
with open(analysis_path, 'w') as analysis_file:

    # print rows in text file
    analysis_file.write("Financial Analysis \n")
    analysis_file.write("---------------------------- \n")
    analysis_file.write("Total Months: %s \n" % (total_months))
    analysis_file.write("Total: $%s \n" % (total_value))
    analysis_file.write("Average Change: $%s \n" % (text_ave))
    analysis_file.write("Greatest Increase in Profits: %s ($%s) \n" % (max_change[0], (final_inc)))
    analysis_file.write("Greatest Decrease in Profits: %s ($%s) \n" % (min_change[0], (final_dec)))