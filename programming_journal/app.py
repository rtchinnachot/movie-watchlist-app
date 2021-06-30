from database import create_table, add_entry, get_entries

menu = """Please select the following
    1) Add new entries for today.
    2) View entries.
    3) Exit.
 
Your selection: """

welcome = "Welcome to programming dairy"

create_table()

def prompt_user_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f'{entry[1]}\n{entry[0]}\n\n')


print(welcome)

# user_input = input(menu)
while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_user_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")

