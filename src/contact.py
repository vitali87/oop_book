from __future__ import annotations


class ContactList(list["Contact"]):
    def search(self, name: str) -> list[Contact]:
        return [contact for contact in self if name in contact.name]


class Contact:
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"f")"
        )
