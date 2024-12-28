import yaml
from tkinter import *

def run_advancement(factions):
    return

class Campaign:

    def __init__(self, crew, faction_list,
                 time, roll, event):
        """
        This is used to define the current campaign.
        Args:
            - Crew
            - Factions
            - Time in weeks
            - Roller Results
            - Event prompts(AI powered)
        """

class Faction:

    def __init__(self, name, tier, description,
                 turf, npcs, notable_assets,
                 quirks, allies, enemies,
                 situation, clocks):
        """
        The faction class will take in information from
        the setting YAML.
        Args:
            - A lot lol
        """
        self.name = name
        self.tier = tier
        self.description = description
        self.turf = turf
        self.npcs = npcs
        self.noteable = notable_assets
        self.quirks = quirks
        self. allies = allies
        self.enemies = enemies
        self.situation = situation
        self.clocks = clocks

class Game:

    def __init__(self):
        """
        This class defines the current instance of the game.
        Args:

        """

    def load_faction_stats(self, faction_list, faction_entry):
        """
        Accepts an entry from the selected Factions YAML
        and loads it into a dictionary.
        Args:
        - Faction_name: the YAML entry for the faction
        """
        with open(faction_list, 'r') as f:
            factions = yaml.safe_load(f)
            for faction in factions:
                if faction_entry in faction:
                    return faction[faction_entry]
        return None

    def create_faction_object(self, faction_list):
        """
        Takes the dictionary returned from load_faction_stats
        and creates a Faction object for that Game instance.
        Args:
        - faction_stats: dict created by load_faction_stats
        """
        for factions in faction_list:
            # load each faction entry as a dictionary
            # parses it to a new Faction object called
            # name = Faction(self, name = name

    def create_all_factions(self, faction_list):
        for factions in faction_list:
            self.create_faction_object()


# This function is used to start a new Campaign
def new_campaign():
    return

# This function is use to load a Campaign
def load_campaign():
    return

def create_campaign_dialog():
    """
    This function is called by the Create Campaign
    button and creates a new YAML file with entered
    campaign data
    """
    return

def load_campaign_dialog():
    """
    This function is called by the Load Campaign
    button and accesses the appropriate YAML file
    campaign data
    """
    return

# This function will be used to access program settings
def settings():
    return

"""
The below code initializes the main window 
of the app using tkinter and initializes
an instance of Game.
"""
root = Tk()
root.title("Forged Factions")
root.geometry("800x800")

# Left side button frame
left_frame = Frame(root)
left_frame.pack(side="left", fill="y")

# New Campaign Button
new_campaign_button = Button(left_frame, text="New Campaign", command=new_campaign)
new_campaign_button.pack(pady=5)

# Load Campaign Button
load_campaign_button = Button(left_frame, text="Load Campaign", command=load_campaign)
load_campaign_button.pack(pady=5)

# Settings Button
settings_button = Button(left_frame, text="Settings", command=settings)
settings_button.pack(pady=5)

# Center scrollable listbox for factions
faction_list = Listbox(root)
faction_scrollbar = Scrollbar(root, orient="vertical", command=faction_list.yview)
faction_list.config(yscrollcommand=faction_scrollbar.set)
faction_scrollbar.pack(side="right", fill="y")
faction_list.pack(fill="both", expand=True)

# Right side button frame
right_frame = Frame(root)
right_frame.pack(side="right", fill="y")

# Run Advancement Button
run_advancement_button = Button(right_frame, text="Run Advancement", command=run_advancement)
run_advancement_button.pack(pady=5)

# Create New Faction Button
# create_new_faction_button = Button(right_frame, text="Create New Faction", command=create_new_faction)
# create_new_faction_button.pack(pady=5)
#
# # Edit Faction Button
# edit_faction_button = Button(right_frame, text="Edit Faction", command=edit_faction)
# edit_faction_button.pack(pady=5)

root.mainloop()