class Lock:
    def __init__(self):
        self.dial_num = 50
        self.password = 0

    def right(self, turn):
        # Not enough to get to 100
        if self.dial_num + turn < 100:
            self.dial_num += turn
        else:
            turn -= (100 - self.dial_num)
            self.password += (1 + int(turn / 100))
            self.dial_num = (turn % 100)

    def left(self, turn):
        # Starting at 0
        if self.dial_num == 0:
            self.password += int(turn / 100)
            self.dial_num = (-turn % 100)
        # Any other number
        else:
            # Not enough to reach zero
            if self.dial_num - turn > 0:
                self.dial_num -= turn
            else:
                turn -= self.dial_num
                self.password += (1 + int(turn / 100))
                self.dial_num = (-turn % 100)


lock = Lock()

with open("secret-code.txt", "r") as file:
    for line in file:
        turn = int(line[1:])
        if line[0] == "R":
            lock.right(turn)
        else:
            lock.left(turn)
        
        
print(lock.password)