import json
import random
import time

import pyautogui


def move_mouse(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(1)  # Add a delay to ensure actions are registered


def click_coordinates(x, y):
    pyautogui.click(x, y)
    # time.sleep(1)  # Add a delay to ensure actions are registered


def double_click_coordinates(x, y):
    pyautogui.doubleClick(x, y, 1)
    time.sleep(1)  # Add a delay to ensure actions are registered


def main():
    with open("src/config.json") as config_file:
        config = json.load(config_file)

    perk_slots_coordinates = config["perkSlotsCoordinates"]
    perk_coordinates = config["perkCoordinates"]
    pages_coordinates = config["pages_coordinates"]

    for slot, slot_coordinates in perk_slots_coordinates.items():
        print(f"* Processing {slot}...")

        # Click on the slot
        move_mouse(slot_coordinates["x"], slot_coordinates["y"])
        click_coordinates(slot_coordinates["x"], slot_coordinates["y"])

        print(f"* Selected slot: {slot} at {slot_coordinates}")

        # Double-click on page_5 coordinate
        move_mouse(pages_coordinates["page_5"]["x"], pages_coordinates["page_5"]["y"])
        double_click_coordinates(
            pages_coordinates["page_5"]["x"], pages_coordinates["page_5"]["y"]
        )

        print(f"* Selected center page: {pages_coordinates['page_5']}")

        # Click on a randomly chosen page
        random_page = random.choice(list(pages_coordinates.values()))
        move_mouse(random_page["x"], random_page["y"])
        pyautogui.click(random_page["x"], random_page["y"], 2, 1)

        print(f"* Selected random page: {random_page}")

        # Select a random row
        random_row = random.choice(list(perk_coordinates.values()))
        print(f"* Choosen random row: {random_row}")

        # Click on a randomly chosen perk within the selected row
        random_perk = random.choice(list(random_row.values()))
        move_mouse(random_perk["x"], random_perk["y"])
        print(f"* Selected random perk: {random_perk}")

        click_coordinates(random_perk["x"], random_perk["y"])
        print("-----------")
        print("-----------")
    print("Script completed successfully.")


if __name__ == "__main__":
    main()
