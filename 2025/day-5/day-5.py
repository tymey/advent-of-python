class Counter:
    def __init__(self):
        self.total = 0
    
    def up(self):
        self.total += 1

counter = Counter()

def first():
    with open("test-database.txt", "r") as file:
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

def second():
    with open("database.txt", "r") as file:
        ranges = []
        for line in file:
            if line == "\n":
                break
            else:
                split_range = line.replace("\n", "").split("-")
                ranges.append([int(split_range[0]), int(split_range[1])])
        
        def first_elem(list):
            return list[0]

        ranges.sort(key=first_elem)

        i = 1

        while i < len(ranges):
            # Beginning of current is less than or equal to end of previous
            if ranges[i][0] <= ranges[i - 1][1]:
                # End of current is greater than end of previous
                if ranges[i][1] > ranges[i - 1][1]:
                    ranges[i - 1][1] = ranges[i][1]
                
                del ranges[i]
            else:
                i += 1

        total = 0

        for rng in ranges:
            total += (rng[1] - rng[0] + 1)
        
        print(ranges)
        print(total)

second()