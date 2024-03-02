""" Models for CLI bot assistan"""

from collections import UserDict
from exceptions import PhoneNotCorrectError, PhoneNotFound


class Field:
    """Base class for filed"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Name class"""


class Phone(Field):
    """Phone class"""

    def __init__(self, phone):
        if not len(phone) == 10 or not phone.isnumeric():
            raise PhoneNotCorrectError
        super().__init__(phone)


class Record:
    """Class for record"""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        """Add new phone object"""
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        """Remvoe phone from list"""
        self.phones.remove(phone)

    def edit_phone(self, current_phone, new_phone):
        """Edit exist phone object"""
        for phone in self.phones:
            if phone.value == current_phone:
                phone.value = new_phone

    def find_phone(self, searching_phone):
        """Find phone in records"""
        for phone in self.phones:
            if phone.value == searching_phone:
                return phone
        raise PhoneNotFound


class AddressBook(UserDict):
    """Address book"""

    def list_contacts(self):
        """Return list of contacts"""
        return self.data

    def add_record(self, record):
        """Adding record to address book"""
        self.data.update({record.name.value: record})

    def find(self, record_key):
        """Find record in list"""
        return self.data.get(record_key)

    def delete(self, record):
        """Deleting record from liss"""
        self.data.pop(record)
