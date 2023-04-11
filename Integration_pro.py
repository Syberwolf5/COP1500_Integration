# Myles Vinal
# A text based dungeon delving adventure game
# most of the # items are intended code, but I lack knowledge
# needed for sprint 1(%)
# Sprint requirement code
print("Date of code creation: " + "2", "8", "2023", sep=("-"))
# sep=("") function changes the , function in print statements what ever is put in the quotes in the ()
# the % operator is modulus which divides the numbers and keeps the remainder
damage = 0  # to be changed
actions = 0  # to be changed
def search_desc():
    per_desc1 = "You see some coins scattered near a skeleton clad in rusted armor"
    per_desc2 = "You see "
    return per_desc1,per_desc2
import random

def main():
    print('Welcome to Dungeon Crawl!')
    start = input("Would you like to start your adventure? Y/N", end=("\n"))
    if start == "Y":
        player_name = input("What is your adventurer's name? ")
        character_stats()
    elif start == "N":
    return player_name

# STATS  section
def character_stats():
    loop = 0
    print("What are their stats?", "\n" + "Total stat point: 25", end=("\n"))
    # stats will affect everything(Health/Damage/Actions)
    while loop == 0:
        end = int(input("In a scale of 1-10, enter a ENDURANCE value: "))
        strg = int(input("In a scale of 1-10, enter a STRENGTH value: "))
        per = int(input("In a scale of 1-10, enter a PERCEPTION value: "))
        kno = int(input("In a scale of 1-10, enter a KNOWLEDGE value: "))
        con = int(input("In a scale of 1-10, enter a MAGIC value: "))
        total_stats = end + strg + per + kno + con
        if total_stats == 25:
            loop = 1
        elif total_stats < 25:
            print("You have unspent stat points")
        else:
            print("Please reselect stats")
    return end, strg, per, kno, con


def stat_counter(endu,streg,con,mana_drain):
    max_hit_points = (endu * streg) // 2
    hit_points = (max_hit_points - damage)
    print("Health: " + ("[]" * hit_points))
    max_stamina = (endu + (streg // 2))
    stamina = (max_stamina - actions)
    print("Stamina: " + ("[]" * stamina))
    max_mana = (con ** 2) / con
    mana = (max_mana - mana_drain)
    print("Mana: " + ("[]" * mana))
    return mana,damage,

# this code above makes the health, magic, and stamina bars, changing values based on damage and actions

# Actions section
def actions(per):
    print("What will you do?: \n(1)Search(PER) \n(2)Move \n(3)Inventory")
    action = int(input("Enter number to corresponding action: "))
    if action == 1:
        if per > 2:
            print()
    elif action == 2:
        movement()
    elif action == 3:
        inventory()
    else:
        print("Incorrect Input")

# Room section(room is letter)
def rooms()
    roomA = "The room is completely dark."
    roomB = "The room is dimly lit by torches on the walls."
    roomC = ""
    return roomA,roomB,roomC

# Movement
def movement():


# combat
def combat():

#enemy function
def enemy(e_health):
    while e_health != 0 or e_health < 0:


main()