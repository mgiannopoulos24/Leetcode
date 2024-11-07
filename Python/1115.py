from threading import Event, Lock

class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_done = Event()
        self.bar_done = Event()
        self.lock = Lock()
        self.foo_done.set()  # Allow foo to run first

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.foo_done.wait()  # Wait for the signal to print "foo"
            printFoo()
            self.bar_done.set()  # Signal that "foo" is done and "bar" can proceed
            self.foo_done.clear()  # Prevent further "foo" prints until "bar" completes

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.bar_done.wait()  # Wait for the signal that "foo" has finished
            printBar()
            self.foo_done.set()  # Signal that "bar" is done and "foo" can proceed
            self.bar_done.clear()  # Prevent further "bar" prints until "foo" completes
