from __future__ import annotations

from typing import Any

from src.contact import ContactList

class Contact:
    all_contacts = ContactList()

    def __init__(
            self,
            /,
            name: str = "",
            email: str = "",
            **kwargs: Any
    ) -> None:
        super().__init__(**kwargs) # type: ignore [call-arg]
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"f")"
        )

class AddressHolder:
    def __init__(
            self,
            /,
            street: str = "",
            city: str = "",
            state: str = "",
            code: str = "",
            **kwargs: Any
    ) -> None:
        super().__init__(**kwargs) #type: ignore [call-type]
        self.street = street
        self.city = city,
        self.state = state,
        self.code = code


class Friend(Contact,AddressHolder):
    def __init__(
            self,
            /,
            phone: str = "",
            **kwargs: Any
     ) -> None:
        super().__init__(**kwargs)
        self.phone = phone