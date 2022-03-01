from __future__ import annotations
from Contact import Contact
from typing_extensions import Protocol

class Emailable(Protocol):

    """
    This means that the class with which the mixin goes must have this attribute
    The 'Protocol' ensures that subclasses (e.g MailSener) support this attribute
    """
    email: str

class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f"sending mail to {self.email}")

class EmailableContact(Contact, MailSender):

    """
    This class basically orchestrates the mixin with the Contact class
    Main functionality provided by the mixin class func
    """
    pass