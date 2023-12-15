import random


# 435 height
# 168


def load_perks():
    # Assuming you have a list of perks or a database of perks
    # Load perks from your source (file, database, etc.)
    perks = [
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
        "Perk16",
        "Perk17",
        "Perk18",
        "Perk19",
        "Perk20",
        # Add more perks as needed
    ]
    return perks


def randomly_select_perks(perks, num_perks=4):
    # Shuffle the list of perks
    random.shuffle(perks)

    # Select the first 4 perks from the shuffled list
    selected_perks = perks[:num_perks]

    return selected_perks


def display_perks(selected_perks):
    # Display the selected perks
    print("Selected Perks:")
    for i, perk in enumerate(selected_perks, 1):
        print(f"{i}. {perk}")


def main():
    perks = load_perks()
    selected_perks = randomly_select_perks(perks)
    display_perks
