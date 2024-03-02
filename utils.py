""" Main functions for CLI bot"""

from datetime import datetime
from datetime import timedelta
from collections import defaultdict
from exceptions import PhoneNotCorrectError, ContactAlredyExist, ContactNotFound
from models import Record


### Home Work 2  / 1
def input_error(func):
    """Return error message if some function does not work with given args"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Given name not found in contacts"
        except IndexError:
            return "Enter user name"
        except PhoneNotCorrectError:
            return "Given telephone number not correct"
        except ContactAlredyExist:
            return "Cannot add new contact. Alredy exist"
        except ContactNotFound:
            return "Cannot not found."

    return inner


def get_birthdays_per_week(users):
    """Return names of users that you need to greet with birstday"""
    days_of_birthday = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year.weekday() in range(5, 7):
                days_to_append = 7 % birthday_this_year.weekday()
                birthday_this_year = birthday_this_year + timedelta(days=days_to_append)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            day_of_week = birthday_this_year.strftime("%A")
            days_of_birthday[day_of_week] += [name]

    for day, users_to_greet in days_of_birthday.items():
        print(f"{day}:", end=" ")
        print(*users_to_greet, sep=", ")


@input_error
def parse_input(user_input):
    """Parse user inputed commands"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    """Add contacts to contact ditictionary"""
    name, phone = args
    if name in contacts:
        return f"Warning: already exist. {change_contact(args, contacts)}"
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Update contact in contacts ditictionary"""
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact updated."
    return f"Contact with name {name} not found. You can add it by command add <name> <number>"


@input_error
def show_phone(name, contacts):
    """Show phone by name"""
    return contacts[name[0]]


@input_error
def show_all(contacts):
    """Show all conatacts"""
    info = ""
    for name, phone in contacts.items():
        info += f"{name}: {phone}\n"
    return info.removesuffix("\n")


# Functions for Home Work 2 / 2
@input_error
def handle_add(book, *args):
    """Add record to address book"""
    name, phone = args
    if book.find(name):
        raise ContactAlredyExist
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)

    return "Contact added."


@input_error
def show_all_addresess(
    book,
):
    """Show all records in book"""
    info = ""
    for _, record in book.data.items():
        info += f"{record}\n"
    return info.removesuffix("\n")


@input_error
def find_record(book, name):
    """Show all address record in book"""
    record = book.find(name)
    if not record:
        raise ContactNotFound
    return record


@input_error
def change_record_phone(book, name, phone, new_phone):
    """Change phone for record"""
    record = book.find(name)
    if not record:
        raise ContactNotFound
    record.edit_phone(phone, new_phone)
    return "Phone has been updated."


@input_error
def add_phone(book, name, phone):
    """Adding new other phone to contact record"""
    record = book.find(name)
    if not record:
        raise ContactNotFound
    record.add_phone(phone)
    book.add_record(record)
    return "Phone has been added."


@input_error
def remove_phone(book, name, phone):
    """Removing phone form contact record"""
    record = book.find(name)
    if not record:
        raise ContactNotFound
    record.remove_phone(phone)
    book.add_record(record)
    return "Phone has been deleted."


@input_error
def delete_address(book, name):
    """Deleting address in book"""
    book.delete(name)
    return "Contact deleted."
