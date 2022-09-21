# Imported datetime to get todays date
from datetime import date

# Declare a dictionary for all the usernames and passwords.
# Read data from file to dictionary reading the passwords as values
# and the usernames as keys.
# Request user input to provide username and password and check if there is
# a match in the dictionary.
# Once correct username with matching password is entered print menu to
# console.
users_dict = {}
with open("user.txt", "r") as users_file:

    for line in users_file:
        data = line.split(", ")
        users_dict[data[0]] = data[1].replace("\n", "")

print("-"*80)
while True:
    username = input("Please enter a username: \n")
    print("-"*80)
    if username in users_dict:
        password = input("Enter your password: \n")
        print("-"*80)
        if password == users_dict[username]:
            break
        else:
            print("Password is incorrect!")
            print("-"*80)
    else:
        print("Username is incorrect!")
        print("-"*80)
        
        
        
# Main while loop that requests input from user to select a option
# from the menu below. If a wrong option was chosen print error
# to console and as to choose again.
# If 'e' is chosen the program will close.
# "ds - Display Statistics" will only print for admin
# Input is taken to lowercase to prevent errors

while True:
    print(("*"*33)+ "TASK STORAGER"+ ("*"*34) + "\n")
    print('''Select one of the following Options below:
 _______________________                 
|r  - Registering a user|
|a  - Adding a task     |
|va - View all tasks    |
|vm - view my task      |''')
    if username == "admin":
        print("|ds - Display Statistics|")
    print("|e  - Exit              |") 
    menu = input("|_______________________| \n\n>").lower()



    if menu == 'r':
        # Check to see if user is admin and Request user to provide
        # username and password and confirm pass word for a new 
        # user.
        # once all information is recieved from user write data to a
        # file "user.txt"
        # Print message to cosole telling user that the new user has
        # been registered 
        
        
        if username == "admin":
            print("-"*80)
            new_username = input("Enter a username: \n")
            print("-"*80)
            new_password = input("Enter a password: \n")
            print("-"*80)
            confirm_pw = input("Please confirm password: \n")
            print("-"*80)
            while new_password != confirm_pw:
                confirm_pw = input("Confirmation password is incorrect! \n"
                                   "Please confirm your password: \n")
                print("-"*80)
            
            # Learned how to open file in append mode to not overwrite current
            # data in file
            with open("user.txt", "a") as users_file:
                users_file.write(f"{new_username}, {new_password}\n")
            
            print("-"*80)
            print("User Registered.")
            print("-"*80)
        
        else:
            print("-"*80)
            print("You are not Admin! You cannot register new users!")
            print("-"*80)

    elif menu == 'a':  
        # Request input from user to provide the following:
        # Task, user for whom the task is for, description of task,
        # due date for task, and if task is completed or not.
        # The due date goes throug a basic total character check
        # and checks if the month is smaller than or equal to 12
        # to determine if date entered is in correct format
        # The assigned date is today's date obtained by using
        # date.today() and using strftime to have it in the 
        # correct format.
        # After all dota is recieved read data to a text file
        # "tasks.txt" in the correct order seperated with ", "
        # Print message to console informing user that the
        # task was saved
        
        month_dict = { 1: "Jan", 2: "Feb", 3: "Mar", 4:"Apr", 5:"May",
                       6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct",
                       11: "Nov", 12: "Dec"}
        
        due_month = 13
        user = input("Enter a user to assign a task to: \n")
        print("-"*80)
        task_title = input("Enter the title for your task: \n")
        print("-"*80)
        task = input("Enter task description: \n")
        print("-"*80)
        date_assigned = (date.today()).strftime("%d %b 20%y")
        due_date = input("Enter the due date for the task? (DD/MM/YYYY) \n") 
        if due_date[3:5]:
            due_month = int(due_date[3:5])
        while len(due_date) != 10 or due_month > 12:
            due_date = input("Date entered in wrong format:" 
                            "Please enter date again:(DD/MM/YYYY) \n")
            if due_date[3:5]:
                due_month = int(due_date[3:5])            
        else:
            due_date = due_date.replace(" ", "/").split("/")              
        due_month = month_dict[int(due_date[1])]
        due_date = f"{due_date[0]} {due_month} {due_date[2]}"  
        print("-"*80)   
        is_complete = input("Is the task completed? Yes/No \n").capitalize()
        print("-"*80)
        with open("tasks.txt", "a") as task_file:
            task_file.write(f"{user}, {task_title}, {task}, {date_assigned}"
                        f", {due_date}, {is_complete}\n")
        
        print("Task stored.")
        print("-"*80)
        

    elif menu == 'va':
        # Read all the lines in the "tasks.txt" file using a for loop
        # and print the data to console in a neat readable manner.
        content = []
        total_tasks = 0
        print("-"*80)
        print("Viewing all tasks:")
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                total_tasks += 1
                content = line.split(", ")
                task_complete = content[5].replace("\n","")
                print("-"*80)
                print(f"Task {total_tasks}\n\n"
                    f"Task:            \t{content[1]} \n"
                    f"Assigned to:     \t{content[0]} \n"
                    f"Date Assigned:   \t{content[3]} \n" 
                    f"Due Date:        \t{content[4]} \n"
                    f"Task Complete?   \t{task_complete} \n"
                    f"Task Description: \n{content[2]}")
            print("-"*80)
        print(f"Total tasks: {total_tasks}")
        print("-"*80)
                

    elif menu == 'vm':
        # Read all the lines in the "tasks.txt" file using a for loop
        # if the user in the line is the same as the logged in user
        # print the task to console.
        content = []
        total_tasks = 0
        print("-"*80)
        print(f"Viewing all tasks for {username}")
        with open("tasks.txt", "r") as task_file:
            print("-"*80)
            for line in task_file:
                content = line.split(", ")
                task_complete = content[5].replace("\n","")
                if content[0].lower() == username.lower():
                    total_tasks += 1
                    print(f"Task {total_tasks}\n\n"
                        f"Task:            \t{content[1]} \n" 
                        f"Assigned to:     \t{content[0]} \n" 
                        f"Date Assigned:   \t{content[3]} \n" 
                        f"Due Date:        \t{content[4]} \n" 
                        f"Task Complete?   \t{task_complete} \n"
                        f"Task Description: \n{content[2]}")
                    print("-"*80)        
        print(f"You have {total_tasks} task/s.")
        
    elif menu == 'ds' and username == "admin":
        # Chech to see if logged in user is admin
        # Count the amount of lines in the task and user file to get
        # the number of tasks and users and print the results to
        # console.
        total_users = 0
        total_tasks = 0
        
        print("-"*80)
        print("Statistics: \n")
        with open("user.txt", "r") as user_file:
            for line in user_file:
                total_users += 1
        
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                total_tasks += 1
        
        print(f"Total Users : \t{total_users}\n" +
            f"Total Tasks : \t{total_tasks}")
        print("-"*80)
        

    elif menu == 'e':
        print("-"*80)
        print('Goodbye!!!')
        print("-"*80)
        exit()

    else:
        print("-"*80)
        print("You have made a wrong choice, Please Try again")
        print("-"*80)