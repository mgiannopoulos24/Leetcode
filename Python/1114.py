from threading import Event

class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # Print "first"
        printFirst()
        # Signal that the first method is done
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait until the first method is done
        self.first_done.wait()
        # Print "second"
        printSecond()
        # Signal that the second method is done
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait until the second method is done
        self.second_done.wait()
        # Print "third"
        printThird()
