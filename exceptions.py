""" Execption for CLI bot"""


class PhoneNotCorrectError(Exception):
    """Phone not mathch error"""


class ContactAlredyExist(Exception):
    """Contac alredy exist in address book"""


class ContactNotFound(Exception):
    """Contact not found"""


class PhoneNotFound(Exception):
    """Not found phones in records"""
