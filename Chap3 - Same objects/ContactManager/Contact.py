from __future__ import annotations
from typing import List
from unicodedata import name

class ContactList(List["Contact"]):

    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

    def searchByName(self, name: str) -> list[str]:
        matching_contacts: list[str] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact.name)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )