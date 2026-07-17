# Question
ABILITY = input("""Choose your ability!
Fly
Superjump
Superspeed
Invulnerability
Emotional Intelligence
Write your decision: """).strip().title()
# Response
if ABILITY == "Fly":
    print("You have chosen Fly ability")
    print("+3.0 acrobatics")
elif ABILITY == "Superjump":
    print("You have chosen Superjump ability")
    print("+2.5 acrobatics")
elif ABILITY == "Superspeed":
    print("You have chosen Superspeed")
    print("+2.5 speed")
elif ABILITY == "Invulnerability":
    print("You have chosen Invulnerability")
    print("+3.0 endurance")
elif ABILITY == "Emotional Intelligence":
    print("You have chosen Emotional Intelligence")
    print("+3.0 charisma")
else:
    print("That is not a valid ability!")        
