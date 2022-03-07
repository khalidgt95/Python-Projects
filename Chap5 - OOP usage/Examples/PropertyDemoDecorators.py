class A:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str
    
    @property
    def foo(self) -> str:
        print("Getting {self._name}'s state")
        return self._state
    
    @foo.setter
    def foo(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}")
        self._state = state 