# TODO:
# + Impelement a gui interface for user-friendliness.
# + Impelement an overlay to hide perks picked till game starts.
# + Impelement perk exception selection so players can choose which perks to exclude from the random selection.

# FIXME:
# + Fix the perk selection so it doesn't pick the same perk twice no matter what.
# + Efficiency/Speed/Maintainability improvements.


import json
import random
import time

import pyautogui

time.sleep(5)  # Add a delay to let the user go to the game window


def move_mouse(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(0.5)


def click_coordinates(x, y):
    pyautogui.click(x, y)
    # time.sleep(1)


def double_click_coordinates(x, y):
    pyautogui.doubleClick(x, y, 0.5)
    time.sleep(1)


def main():
    with open("src/config.json") as config_file:
        config = json.load(config_file)

    perk_slots_coordinates = config["perkSlotsCoordinates"]
    perk_coordinates = config["perkCoordinates"]
    pages_coordinates = config["pages_coordinates"]

    for slot, slot_coordinates in perk_slots_coordinates.items():
        print(f"-----Processing {slot}-----")

        # Click on the slot
        move_mouse(slot_coordinates["x"], slot_coordinates["y"])
        click_coordinates(slot_coordinates["x"], slot_coordinates["y"])

        print(f"* Selected {slot}")

        # Double-click on page_5 coordinate
        move_mouse(pages_coordinates["page_5"]["x"], pages_coordinates["page_5"]["y"])
        double_click_coordinates(
            pages_coordinates["page_5"]["x"], pages_coordinates["page_5"]["y"]
        )

        print("* Selected center page: page_5")

        # Click on a randomly chosen page
        random_page = random.choice(list(pages_coordinates.values()))
        move_mouse(random_page["x"], random_page["y"])
        pyautogui.click(random_page["x"], random_page["y"], 2, 0.5)

        print(
            f"* Selected random page: {list(pages_coordinates.keys())[list(pages_coordinates.values()).index(random_page)]}"
        )

        # Select a random row
        random_row = random.choice(list(perk_coordinates.values()))
        print(
            f"* Selected random row: {list(perk_coordinates.keys())[list(perk_coordinates.values()).index(random_row)]}"
        )

        # Click on a randomly chosen perk within the selected row
        random_perk = random.choice(list(random_row.values()))
        move_mouse(random_perk["x"], random_perk["y"])
        print(
            f"* Selected random perk: {list(random_row.keys())[list(random_row.values()).index(random_perk)]}"
        )

        click_coordinates(random_perk["x"], random_perk["y"])
        print("-----------")
        print("-----------")
    print("Script completed successfully.")


if __name__ == "__main__":
    main()
