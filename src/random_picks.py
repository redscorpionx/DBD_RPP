import random

# Assuming perks are stored in a list, where each page is a sublist
all_perks = [
    [
        "Perk1",
        "Perk2",
        "Perk3",
        "Perk4",
        "Perk5",
        "Perk6",
        "Perk7",
        "Perk8",
        "Perk9",
        "Perk10",
        "Perk11",
        "Perk12",
        "Perk13",
        "Perk14",
        "Perk15",
    ],
    [
        "Perk16",
        "Perk17",
        "Perk18",
        "Perk19",
        "Perk20",
        "Perk21",
        "Perk22",
        "Perk23",
        "Perk24",
        "Perk25",
        "Perk26",
        "Perk27",
        "Perk28",
        "Perk29",
        "Perk30",
    ],
]


def pick_random_perks():
    selected_perks = set()

    while len(selected_perks) < 4:
        # Choose a random page
        random_page = random.choice(all_perks)

        # Choose a random perk from the selected page
        random_perk = random.choice(random_page)

        # Add the perk to the set of selected perks
        selected_perks.add(random_perk)

    return list(selected_perks)


# Get the randomly selected perks
selected_perks = pick_random_perks()

# Display the result
print(selected_perks)


# screen size: 1920 x 1080

# Perk slots coordinates
perk_slot_one = (495, 930)
perk_slot_two = (540, 930)
perk_slot_three = (581, 930)
perk_slot_four = (622, 930)


# # perk coordinates on each page

# # perks 1 - 5 (row 1)
perk_one = (392, 630)
perk_two = (515, 630)
perk_three = (643, 630)
perk_four = (764, 630)
perk_five = (885, 630)

# # perks 6 - 10 (row 2)
perk_six = (460, 722)
perk_seven = (581, 722)
perk_eight = (711, 722)
perk_nine = (826, 722)
perk_ten = (958, 722)

# # perks 11 - 15 (row 3)
perk_eleven = (395, 814)
perk_twelve = (517, 814)
perk_thirteen = (645, 814)
perk_fourteen = (771, 814)
perk_fifteen = (887, 814)


# pages coordinates
one = (495, 930)
two = (540, 930)
three = (581, 930)
four = (622, 930)
five = (665, 930)
six = (705, 930)
seven = (746, 930)
eight = (790, 930)
nine = (832, 930)
