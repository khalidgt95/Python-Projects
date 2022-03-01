class BaseClass:
    num_base_calls = 0

    def call_me(self) -> None:
        print("Calling method on base class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on left subclass")

class RightSubclass(BaseClass):

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on right subclass")

class SubClass(LeftSubclass, RightSubclass):

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on sub class")