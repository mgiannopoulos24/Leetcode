import threading

class DiningPhilosophers:
    def __init__(self):
        # Create 5 locks for 5 forks (one between each pair of philosophers)
        self.forks = [threading.Lock() for _ in range(5)]
    
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        # We define left and right fork indices for the current philosopher
        leftFork = philosopher
        rightFork = (philosopher + 1) % 5
        
        # We need to prevent deadlock by enforcing an order of picking up forks
        # For example, philosopher with an even id picks the left fork first
        # and odd ids pick the right fork first.
        
        if philosopher % 2 == 0:
            # Pick left fork first for even philosophers
            with self.forks[leftFork]:
                with self.forks[rightFork]:
                    pickLeftFork()    # Pick the left fork
                    pickRightFork()   # Pick the right fork
                    eat()             # Eat when both forks are held
                    putRightFork()    # Put down the right fork
                    putLeftFork()     # Put down the left fork
        else:
            # Pick right fork first for odd philosophers
            with self.forks[rightFork]:
                with self.forks[leftFork]:
                    pickRightFork()   # Pick the right fork
                    pickLeftFork()    # Pick the left fork
                    eat()             # Eat when both forks are held
                    putLeftFork()     # Put down the left fork
                    putRightFork()    # Put down the right fork
