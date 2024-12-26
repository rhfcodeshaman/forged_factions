Core App Features:
- Dice Roller
- Create/Save/Load Campaigns
- Read Faction Lists
- Create/Edit Faction Lists
- Run Advancement
- Produce events/session prompts based on advancement
Stretch App Features:
- Map Integration
- Turf Wars





1. Input Format:
```
# Factions List (Example)
factions:
  - name: The Hawkhurst Crew (Tier 3)  # Faction Name with Tier in parentheses
    tier: 3  # Tier as a number (0-6)
    description: >  # Multi-line description using folded style
      A ruthless crew of privateers who prey on merchant ships 
      along the Kingfisher Route. 
    turf: The Smuggler's Den  # Turf as a string 
    npcs: >  # NPC list as a multi-line string using folded style
      * Silas "Razor" Quinn - Captain. A cunning and ruthless leader.
      * Ivara, the Navigator - A woman with an uncanny sense of direction. 
    # List of Notable Assets (individual items)
    notable_assets:
      - The Black Pearl - A heavily armed clipper ship.
      - The Cutlass of Captain Blackheart - A legendary pirate blade.
    quirks: >  # Quirks as a multi-line string using folded style
      The crew is known for their love of gambling and their 
      hatred for the Bluecoats (city watch).  
    allies:  # List of Allied Factions
      - The Whisperwind Syndicate
    enemies:  # List of Enemy Factions
      - The Bluecoats  
      - The Kraken's Teeth
    situation: >  # Situation as a multi-line string using folded style
      The Hawkhurst Crew has recently captured a lucrative shipment 
      of spices. However, they've attracted the unwanted attention 
      of both the Bluecoats and a rival pirate crew, the Kraken's Teeth.     
    clocks:  # List of Clocks (name, description, current value, max value)
      - name: Hunting Grounds Established
        description: Establish a network of informants and safehouses.
        current: 2  # Current value of the clock (0-16)
        max: 6  # Maximum value to complete the clock (4-6)
      - name: Crew Loyalty
        description: Maintain the loyalty of your crew. 
        current: 9  # Current value of the clock (0-16)
        max: 5  # Maximum value to complete the clock (4-6)


```
2. Parser: PyYaml
3. Dice Roller:
```
import random

def roll_dice(tier):
  """
  Rolls a pool of dice based on the tier and interprets the result for clock advancement.

  Args:
      tier: The tier of the faction (integer between 0 and 6).

  Returns:
      An integer representing the amount the clock should tick forward (0, 1, 2, or 3).
  """

  # Ensure tier is within valid range
  if tier < 0 or tier > 6:
    raise ValueError("Tier must be between 0 and 6")

  # Roll the dice pool based on tier
  dice_pool = [random.randint(1, 6) for _ in range(tier + 1)]

  # Find the highest result
  highest_result = max(dice_pool)

  # Determine clock advancement based on highest result
  if highest_result <= 3:
    return 0
  elif highest_result == 4 or highest_result == 5:
    return 1
  elif highest_result == 6:
    # Count the number of 6s
    num_sixes = sum(1 for die in dice_pool if die == 6)
    return 2 if num_sixes == 1 else 3
```