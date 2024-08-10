#importing the os module to interact with os methods for reading and writing with files.
import os

#menu to show when our program loads at first
def showMenu():
    print("*** Choose Any Option from below. ****")
    print("Please select an option.")


#loading department files
def loadAndCalculateDepartmentFiles():
    # Listing all the relevant department files from the project source root folder. ignoring financial_report
    #department_files = [file for file in os.listdir() if file.endswith('.txt') and file != 'financial_report.txt']

    # ignore the previous _avg and failed files to prevent the calculation issue and creating multiple files each time we run the option
    department_files = [file for file in os.listdir() 
                        if file.endswith('.txt') and 
                        file != 'financial_report.txt' and 
                        '_avg' not in file and 
                        '_failed' not in file]
    
    for file in department_files:
        # Extract department code from the file name just taking the everything before . with split
        department_code = file.split('.')[0]
        
        total_q1 = total_q2 = total_q3 = total_q4 = 0
        total_employees = failed_employees = 0
        
        #opening the file for reading mode
        #with handles the file close automatically we are just typecasting it as a variable f here
        with open(file, 'r') as f:
            next(f)  # Skiping the header line because of the quaters title
            
            for line in f:
                data = line.split()
                if len(data) == 5:
                    q1, q2, q3, q4 = map(float, data[:4])
                    employee_id = data[4]
                    
                    total_q1 += q1
                    total_q2 += q2
                    total_q3 += q3
                    total_q4 += q4
                    total_employees += 1
                    
                    total_revenue = q1 + q2 + q3 + q4
                    #if the total revenue is less than 80000 then increase the failed employees by 1
                    if total_revenue < 80000:
                        failed_employees += 1
        # Calculate averages
        avg_q1 = total_q1 / total_employees if total_employees else 0
        avg_q2 = total_q2 / total_employees if total_employees else 0
        avg_q3 = total_q3 / total_employees if total_employees else 0
        avg_q4 = total_q4 / total_employees if total_employees else 0
        
         # Write averages to file
        avg_file = f"{department_code}_avg.txt"
        with open(avg_file, 'w') as f:
            f.write(f"Average Q1 Revenue: {avg_q1:.2f}\n")
            f.write(f"Average Q2 Revenue: {avg_q2:.2f}\n")
            f.write(f"Average Q3 Revenue: {avg_q3:.2f}\n")
            f.write(f"Average Q4 Revenue: {avg_q4:.2f}\n")
        
        # Write failed employees count to file
        failed_file = f"{department_code}_failed.txt"
        with open(failed_file, 'w') as f:
            f.write(f"Number of employees who did not meet the annual revenue target: {failed_employees}\n")
        
        print(f"CREATED {department_code}: Averages and failed employees files created.")


#method for searching keyword
def searchAndFindKeywordInReport():
    try:
        file = open("financial_report.txt", "r")
        report_lines = file.readlines()
        #close the program after reading
        file.close() 
        
        while True:
            keyword = input("Enter a keyword to search (or type 'exit' to quit): ").strip()
            if keyword.lower() == 'exit':
                break
            
            count = sum(line.lower().count(keyword.lower()) for line in report_lines)
            print(f"The keyword '{keyword}' occurred {count} times in the report.")
    # handle exception        
    except FileNotFoundError:
        print("Error: 'financial_report.txt' file not found. Please ensure it is in the correct directory.")




# main method for our program
def main():
    #showing the menu for our program
    showMenu()
    # looping the program until break statement
    while True:
        print("\n****Menu:***")
        print("1. Calculate the average revenue for all department")
        print("2. Search for a keyword in the financial report")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            loadAndCalculateDepartmentFiles()
        elif choice == '2':
            searchAndFindKeywordInReport()
        elif choice == '3':
            print("Exiting the program. Thankyou.")
            #break the loop when they enter 4
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Run the program
main()
