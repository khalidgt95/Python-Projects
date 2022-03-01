from typing import Any, Optional


class Contact:

    def __init__(
        self, 
        name: Optional[str] = "", 
        email: Optional[str] = "",
        **kwargs: Any 
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}("
            f"{self.email!r}("
            ")"
        )

class AddressHolder:

    def __init__(
        self,
        street: str = "",
        city: str = "",
        state: str = "",
        code: str = "",
        **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):

    """
    When initializing classes with different arguments, we pass the kwargs dictionary as the argument
    The basic idea is that all of the params are passed up to the classes
    Each class takes the params it needs from the dict and passes upwards
    At the end, all of the params are guaranteed to be used
    """
    def __init__(
        self,  
        phone: str = "",
        **kwargs: Any
    ) -> None:

        super().__init__(**kwargs)
        self.phone = phone