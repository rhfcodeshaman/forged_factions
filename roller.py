import random

def roll_dice(tier):
    """
    Rolls a pool of dice based on the tier and interprets the result for clock advancement.
    Args:
        tier: The tier of the faction (integer between 0 and 6).
    Returns:
        An integer representing the amount the clock should tick forward (0, 1, 2, or 3).
    """

    # ensure the dice are within a valid range
    if tier < 0 or tier > 6:
        raise ValueError("The tier must between 0 and 6")

    # roll the dice based on tier
    dice_pool = tier
    results = []
    for dice in range(dice_pool):
        dice_roll = random.randrange(1, 7)
        results.append(dice_roll)
    print(results)
    critical_success = (results.count(6) == 2)

    if critical_success == True:
        return 3
        print("A critical success! :)")
    elif max(results) == 6:
        return 2
        print("A success!")
    elif max(results) >= 4:
        return 1
        print("A partial success...")
    elif max(results) <= 3:
        print("A failure... :'(")
        return 0
