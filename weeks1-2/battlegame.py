# Races
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
# HP
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# dragon
dragon_hp = 300
dragon_damage = 50


# orc
orc_hp = 90
orc_damage = 30
"""
WEEK 1 ASSIGNMENT
"""

# input character


while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    character = input("Choose your character:")
    character = character.lower()
    print("\n")
    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break

    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break

    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    #Orc Option (Bonus Task)
    elif character == "4":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break

    #quit game option (Bonus Task)
    elif character == "9":
        print("Exiting game...")
        quit()

    else:
        print("Unknown character, Try again or enter 9 to quit")

print("You have chosen the character: ", character)
print("Health: ", my_hp)
print("Damage: ", my_damage, " \n")

while True:
    if dragon_hp > 0 and my_hp > 0:
        dragon_hp = dragon_hp - my_damage
        my_hp = my_hp - dragon_damage
        print("The ", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now ", dragon_hp, "\n")

        if dragon_hp <= 0:
            continue
        print("The Dragon strikes back at", character)
        print("The", character, "'s hitpoints are now ",  my_hp, "\n\n")
        continue
    elif dragon_hp <= 0:
        print("The Dragon lost the battle")
        break
    else:
        print("The ", character, "lost the battle!")
        break
