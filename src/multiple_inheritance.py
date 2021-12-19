from typing_extensions import Protocol
from Contact import Contact

class Emailable(Protocol):
    email: str

class MailSender(Emailable):
    def send_email(self,message: str) -> None:
        print(f"Sending mail to {self.email=}")
        #Add email logic here

class EmailableContact(Contact,MailSender):
    pass