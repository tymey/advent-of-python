class PaperRolls:
    def __init__(self):
        self.total = 0
        self.matrix = []
        self.done = False
    
    def pick_up_roll(self, y, x):
        self.total += 1
        self.matrix[y][x] = '.'

    def search(self, num, keep_searching=False):
        self.done = True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.check(i, j, num, keep_searching)
    
    def check(self, y, x, num, keep_searching):
        count = 0

        top, left = (y == 0), (x == 0)
        bottom, right = (y == (len(self.matrix) - 1)), (x == (len(self.matrix[y]) - 1))

        if not top and not left and self.matrix[y - 1][x - 1] == "@":
            count += 1
        if not top and self.matrix[y - 1][x] == "@":
            count += 1
        if not top and not right and self.matrix[y - 1][x + 1] == "@":
            count += 1
        if not right and self.matrix[y][x + 1] == "@":
            count += 1
        if not right and not bottom and self.matrix[y + 1][x + 1] == "@":
            count += 1
        if not bottom and self.matrix[y + 1][x] == "@":
            count += 1
        if not bottom and not left and self.matrix[y + 1][x - 1] == "@":
            count += 1
        if not left and self.matrix[y][x - 1] == "@":
            count += 1

        if count < num and self.matrix[y][x] == "@":
            self.pick_up_roll(y, x)
            if keep_searching:
                self.done = False

paper_rolls = PaperRolls()

with open("paper-rolls.txt", "r") as file:
    roll_matrix = []
    for line in file:
        split_line = list(line)
        roll_matrix.append(split_line[:-1]) if split_line[-1] == "\n" else roll_matrix.append(split_line)
    paper_rolls.matrix = roll_matrix
    
    while not paper_rolls.done:
        paper_rolls.search(4, keep_searching=True)

    print(paper_rolls.total)