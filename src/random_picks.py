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


def pick_random_perks(num_perks_to_pick):
    selected_perks = set()

    while len(selected_perks) < num_perks_to_pick:
        # Choose a random page
        random_page = random.choice(all_perks)

        # Choose a random perk from the selected page
        random_perk = random.choice(random_page)

        # Add the perk to the set of selected perks
        selected_perks.add(random_perk)

    return list(selected_perks)


# Number of perks to pick
num_perks_to_pick = 4

# Get the randomly selected perks
selected_perks = pick_random_perks(num_perks_to_pick)

# Display the result
print("Randomly Selected Perks:", selected_perks)
