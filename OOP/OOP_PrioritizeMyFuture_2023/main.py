from src.User import User, RegistrationUser

a = RegistrationUser()
a.add_task("hello")

"""
# validate user login
if not validate_login(username, password):
    print("Invalid username or password. Exiting.")
    return

# create user object
user = User(username, password)

# get start time
start_time = get_start_time()
remaining_time = get_remaining_time(start_time)

print(f"Welcome, {username}! You have {remaining_time} minutes left in your day.")

while True:
    # print menu
    print("\nChoose an option:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

    # get user input
    choice = input("> ")

    # handle user choice
    if choice == "1":
        add_task(user)
    elif choice == "2":
        remove_task(user)
    elif choice == "3":
        view_tasks(user)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
"""

if __name__ == '__main__':
    print('PyCharm')

