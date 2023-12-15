import json
import random
import time

import pyautogui

# Load config from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)


# Function to click on a given coordinate
def click_coordinate(x, y):
    pyautogui.click(x, y)
    time.sleep(1)  # Wait for the action to complete


# Function to select a random perk from a given row
def select_random_perk(row):
    perk_list = list(config["perkCoordinates"][row].keys())
    random_perk = random.choice(perk_list)
    return config["perkCoordinates"][row][random_perk]


# Function to select a random page
def select_random_page():
    page_list = list(config["pages_coordinates"].keys())
    random_page = random.choice(page_list)
    return config["pages_coordinates"][random_page]


# Function to select perks for all four slots
def select_perks():
    for i in range(1, 5):
        # Select perk slot
        slot = f"slot_{i}"
        slot_coordinates = config["perkSlotsCoordinates"][slot]
        click_coordinate(slot_coordinates["x"], slot_coordinates["y"])

        # Select random page
        page_coordinates = select_random_page()
        click_coordinate(page_coordinates["x"], page_coordinates["y"])

        # Select random perk from each row
        for row in config["perkCoordinates"]:
            perk_coordinates = select_random_perk(row)
            click_coordinate(perk_coordinates["x"], perk_coordinates["y"])


# Run the script
select_perks()
