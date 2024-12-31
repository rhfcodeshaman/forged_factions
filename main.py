import yaml
import shutil
from tkinter import *

# This function is used to start a new Campaign
def new_campaign(setting, campaign_name):
    """
    This function creates a new campaign from the given setting
    Args:
        - setting
        - campaign_name
    """
    # Loads the variables passed to this function as the filepaths
    save_file_info = './save_files/example.yaml'
    base_faction_list = './default_factions/' + setting + '.yaml'
    save_file = './save_files/' + campaign_name + '.yaml'

    # Algorithm needed to append campaign_name to
    # 'campaign' and a datestamp to 'date' as
    # well as create new filepath for the save
    # possibly add save number to this?

    # Copies the content into a NEW save
    shutil.copyfile(save_file_info, save_file)
        with open(save_file, 'a') as save, open(base_faction_list, 'r') as base:
        save.write('\n')
        save.write(base.read())

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

def load_faction_stats(campaign):
    """
    Accepts an entry from the selected Factions YAML
    and loads it into a dictionary from the Class
    Factions.
    Args:
    - campaign: the name of the loaded campaign
    - faction_list: the YAML entry for the factions
    """
    save = ('./save_files/' + campaign + ".yaml")
    with open(save, 'r') as s:
        save_file = yaml.safe_load(s)
        faction_list = save_file['save']['filepath']
    with open(faction_list, 'r') as f:
        factions = yaml.safe_load(f)

def run_advancement(factions):
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