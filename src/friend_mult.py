from src.contact import Contact
from src.address_holder import AddressHolder

class Friend(Contact,AddressHolder):
    def __init__(
            self,
            name: str,
            email: str,
            phone: str,
            street: str,
            city: str,
            state: str,
            code: str
    ) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone