# Dead By Daylight Random Perk Picker

Implementation of the random perks dbd devs refuse to give us!

## TODO:
- Impelement a gui interface for user-friendliness.
- Impelement an overlay to hide perks picked till game starts.
- Impelement perk exception selection so players can choose which perks to exclude from the random selection.
- Impelement a killer version of the script.
- Impelement a version of the script that works on all resolutions.

## Usage

- This only works on a 1920x1080 resolution.
- Before running the script, make sure you are on the perk selection page of the game.
- When you run the script, you have 5 seconds to click on the game window before the script starts picking random perks.
- The script will pick 4 random perks for you.
- This is the first version of the script, so it is not perfect.
- i tested on survivor only, 9 pages of perks. killer 🤷‍♂️

### activate your environment
```python -m venv venv```

```source venv/bin/activate```

### install requirements
```pip install -r requirements.txt```

### run the script
```cd Dead By Daylight Random Perk Picker/src```

```python random_picks.py``` 

