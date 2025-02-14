# Quiz on Conditions

# Write a Python program to check if a player Lionel Messi has more than 10 achievements. If the condition is true, print the player's name, sport, and achievements else print does not have more than 10 achievements.

player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(f"{player_name} {sport} {achievements}")
else:
    print("Does not have more than 10 achievements")

# Write a Python program to check if a player belongs to the sport Tennis or has exactly 20 achievements. If the condition is true, print a success message.
player_tennis = "Roger Federer"
sport_tennis = "Tennis"
achievements_t = 20

if sport_tennis == "Tennis" and achievements_t == 20:
    print("Sucessfull")
else:
    print("Does not meet the condition")

# Write a Python program to check if a player has less than 10 achievements and does not play Soccer. Print their details if they meet the criteria.
player_any = "Usain Bolt"
sport_any = "Athletics"
achievements_any = 8

if achievements_any < 10 and not sport_any == "Soccer":
    print(f"{player_any} plays {sport_any} and has only {achievements_any} achievements")
else:
    print(f"{player_any} doenst meet the criteria")