class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.direction = "East"
        self.directions = ["East", "North", "West", "South"]
        self.dir_index = 0
        self.perimeter = 2 * (width + height - 2)  # Total steps for one full cycle

    def step(self, num: int) -> None:
        if num >= self.perimeter:
            num %= self.perimeter
            # Handle edge case where num becomes 0 after modulo
            if num == 0 and (self.x == 0 and self.y == 0):
                # If the robot is at (0, 0) and num is a multiple of the perimeter,
                # it means the robot has completed full cycles and should face South.
                self.direction = "South"
                self.dir_index = 3

        for _ in range(num):
            next_x, next_y = self.x, self.y
            if self.direction == "East":
                next_x += 1
            elif self.direction == "North":
                next_y += 1
            elif self.direction == "West":
                next_x -= 1
            elif self.direction == "South":
                next_y -= 1

            if 0 <= next_x < self.width and 0 <= next_y < self.height:
                self.x, self.y = next_x, next_y
            else:
                # Turn 90 degrees counterclockwise
                self.dir_index = (self.dir_index + 1) % 4
                self.direction = self.directions[self.dir_index]
                # Retry the step after turning
                self.step(1)

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction