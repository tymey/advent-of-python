class CodeList:
    def __init__(self):
        self.list = []
    
    def add(self, id):
        self.list.append(id)

    def sum(self):
        return sum(self.list)

invalid_codes = CodeList()

def check_silly_code(id):
    groups = []
    for i in range(1, int(len(id) / 2) + 1):
        if len(id) % i == 0:
            group = []
            for j in range(0, len(id), i):
                group.append(id[j:j + i])
            groups.append(group)
    for grp in groups:
        if len(set(grp)) == 1:
            invalid_codes.add(int(id))
            break

with open("ranges.txt", "r") as file:
    file_string = file.read()

ranges = file_string.split(",")

for rng in ranges:
    bookends = rng.split("-")
    start = int(bookends[0])
    end = int(bookends[1])
    for i in range(start, end):
        check_silly_code(str(i))

# print(f"{invalid_codes.list}")
print(f"{invalid_codes.sum()}")