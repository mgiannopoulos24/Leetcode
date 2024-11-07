import threading

class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.state = 0  # 0 - printing zero, 1 - printing odd, 2 - printing even
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def zero(self, printNumber: callable):
        for i in range(1, self.n + 1):
            with self.condition:
                self.condition.wait_for(lambda: self.state == 0)
                printNumber(0)
                self.state = 1 if i % 2 == 1 else 2
                self.condition.notify_all()

    def even(self, printNumber: callable):
        for i in range(2, self.n + 1, 2):
            with self.condition:
                self.condition.wait_for(lambda: self.state == 2)
                printNumber(i)
                self.state = 0
                self.condition.notify_all()

    def odd(self, printNumber: callable):
        for i in range(1, self.n + 1, 2):
            with self.condition:
                self.condition.wait_for(lambda: self.state == 1)
                printNumber(i)
                self.state = 0
                self.condition.notify_all()
