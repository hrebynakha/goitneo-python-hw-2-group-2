"""
The Python bot helper
"""

from models import AddressBook
from utils import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    handle_add,
    show_all_addresess,
    change_record_phone,
    add_phone,
    delete_address,
    remove_phone,
)


def main_hw_2_1():
    """Main function for check Home work #2/1"""
    # get_birthdays_per_week(users_list)
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


def main():
    """Main function in Home work #2/2"""
    print("Welcome to the assistant bot!")
    book = AddressBook()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handle_add(book, *args))
        elif command == "all":
            print(
                show_all_addresess(
                    book,
                )
            )
        elif command == "change":
            print(change_record_phone(book, *args))
        elif command == "addphone":
            print(add_phone(book, *args))
        elif command == "removephone":
            print(remove_phone(book, *args))
        elif command == "del":
            print(delete_address(book, *args))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
