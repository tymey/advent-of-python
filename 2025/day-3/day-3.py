class Jolts:
    def __init__(self):
        self.list = []

    def add(self, max_jolt):
        self.list.append(max_jolt)

    def sum(self):
        return sum(self.list)

def find_max_jolt_two_digit(bank):
    bank_list = list(bank)
    # Find max number (excluding last digit)
    first_num = max(bank_list[:-2])
    # Find the first index of that number
    i = bank_list.index(first_num)
    # Then find the max number after that index
    second_num = max(bank_list[i + 1:])
    # Concatenate both numbers
    max_jolt = first_num + second_num
    # Return cast to int
    return int(max_jolt)

def find_max_jolt(bank, digits):
    bank_list = list(bank)
    if bank_list[-1] != "\n":
        bank_list.append("\n")
    max_jolt_list = []
    moving_index = 0
    for i in range (digits, 0, -1):
        max_number = max(bank_list[moving_index:-i])
        moving_index = bank_list.index(max_number, moving_index) + 1
        max_jolt_list.append(max_number)
    return int("".join(max_jolt_list))

max_jolts = Jolts()

with open("banks.txt", "r") as file:
    for line in file:
        max_jolts.add(find_max_jolt(line, 12))

print(max_jolts.list)
print(max_jolts.sum())