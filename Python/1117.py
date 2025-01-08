from threading import Condition

class H2O:
    def __init__(self):
        self.cond = Condition()  # Condition variable
        self.h_count = 0         # Counter for hydrogen atoms
        self.o_count = 0         # Counter for oxygen atoms

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.cond:
            # Wait until there are fewer than 2 hydrogen atoms available for pairing
            while self.h_count == 2:
                self.cond.wait()

            # Add a hydrogen atom
            self.h_count += 1
            self._try_form_water()

        # Release hydrogen atom
        releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.cond:
            # Wait until no oxygen atom is available for pairing
            while self.o_count == 1:
                self.cond.wait()

            # Add an oxygen atom
            self.o_count += 1
            self._try_form_water()

        # Release oxygen atom
        releaseOxygen()

    def _try_form_water(self):
        # Check if we can form water (2 H and 1 O available)
        if self.h_count == 2 and self.o_count == 1:
            self.h_count -= 2
            self.o_count -= 1
            self.cond.notify_all()  # Notify waiting threads
