class Counter:
    def __init__(self):
        self.total = 0
    
    def up(self):
        self.total += 1

counter = Counter()

with open("database.txt", "r") as file:
    ranges = []
    ids = []
    switch = False
    for line in file:
        if line == "\n":
            switch = True
        else:
            ids.append(line.replace("\n", "")) if switch else ranges.append(line.replace("\n", ""))

    for id in ids:
        match = False
        int_id = int(id)

        for rng in ranges:
            split_range = rng.split("-")
            beg = int(split_range[0])
            end = int(split_range[1])
            if int_id in range(beg, end + 1):
                match = True

        if match:
            counter.up()
    
    print(counter.total)