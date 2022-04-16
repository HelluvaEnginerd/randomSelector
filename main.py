import csv
import random

entry_list = []

random.seed(input("provide random seed string (any numbers and letters): "))

with open('input.csv') as input_file:
    reader = csv.DictReader(input_file, delimiter=',')

    # build list of entries
    for row in reader:
        for i in range(int(row['entries'])):
            entry_list.append(row['name'])

    # # print the list of entries
    # print("unshuffled list of entries\n")
    # for i in range(len(entry_list)):
    #     print(entry_list[i])
    # print("\n\n")

    # shuffle the list
    random.shuffle(entry_list)

    # # print the shuffled list of entries
    # print("shuffled list of entries\n")
    # for i in range(len(entry_list)):
    #     print(entry_list[i])
    # print("\n\n")

    # how many winners do we want
    num_winners = int(input("How many people should win?\n>"))
    print(f"picking {num_winners} winners from {len(entry_list)} entries\n\n")

    # pick the winners
    for i in range(num_winners):
        winner = entry_list.pop(random.randrange(0,len(entry_list)))
        print(f"winner #{i+1} is {winner}")
        list(filter((winner).__ne__, entry_list))

        # #  debugging that {winner} was removed from list
        # print(f"new list after {winner} won")
        # for i in range(len(entry_list)):
        #     print(entry_list[i])
        # print("\n\n")