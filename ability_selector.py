abilities = { 
    'Fly': '+3.0 acrobatics', 
    'Superjump': '+2.5 acrobatics',
    'Superspeed': '+2.5 speed',
    'Invulnerability': '+3.0 endurance',
    'Emotional Intelligence': '+3.0 charisma'
}

# 1. Show the user the available options using the keys
print("Choose your ability:")
for name in abilities.keys():
    print(f"- {name}")

# 2. Get the player's choice
choice = input("Write your decision: ").strip().title()
print("---")

# 3. Look up their choice in the dictionary
if choice in abilities:
    print(f"You have chosen {choice} ability")
    print(abilities[choice])  # This prints the specific value for that key
else:
    print("That is not a valid ability!")
