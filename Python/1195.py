import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                if self.current % 3 == 0 and self.current % 5 != 0:
                    printFizz()
                    self.current += 1
                    self.condition.notify_all()
                else:
                    self.condition.wait()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                if self.current % 5 == 0 and self.current % 3 != 0:
                    printBuzz()
                    self.current += 1
                    self.condition.notify_all()
                else:
                    self.condition.wait()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                if self.current % 3 == 0 and self.current % 5 == 0:
                    printFizzBuzz()
                    self.current += 1
                    self.condition.notify_all()
                else:
                    self.condition.wait()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.condition:
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                if self.current % 3 != 0 and self.current % 5 != 0:
                    printNumber(self.current)
                    self.current += 1
                    self.condition.notify_all()
                else:
                    self.condition.wait()
