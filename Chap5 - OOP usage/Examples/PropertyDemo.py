class S:
    def __init__(self, name: str, age: int) -> None:
        self._age = age
        self._name = name # _name denotes a private attribute

    def _set_name(self, name:str) -> None:  # Function name can be anything
        if name == "" or name == "John":
            raise ValueError("Empty and John are not allowed")
        self._name = name
    def _get_name(self) -> str:
        return self._name

    name = property(_get_name, _set_name)  # position of arguments matter