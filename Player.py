import itemsInfo

class playerStats:   
    maximumHealth = 100 
    health = 100 
    weapon = "Wooden Sword"
    armour = "Cloth Scraps"
    minimumDamage1 = itemsInfo.SwordsDict[weapon]["minDps"]
    maximumDamage1 = itemsInfo.SwordsDict[weapon]["maxDps"]
    damageReduction = itemsInfo.ArmourDict[armour]["dmgRed"]
    minimumDamage = itemsInfo.SwordsDict[weapon]["minDps"]
    maximumDamage = itemsInfo.SwordsDict[weapon]["maxDps"]
    # minimumDamage = 10000
    # maximumDamage = 10001
    level = 1
    xp = 0 

    inventory = {
        "gold": {
            "amount": 100000000,
            "type" : "loot"
        },
        "Minor Health Potion": {
            "amount": 10,
            "type" : "consumable"
        },
        "Lesser Health Potion": {
            "amount": 0,
            "type" : "consumable"
        },
        "Health Potion": {
            "amount": 0,
            "type" : "consumable"
        },
        "Greater Health Potion": {
            "amount": 0,
            "type" : "consumable"
        },
        "Superior Health Potion": {
            "amount": 0,
            "type" : "consumable"
        }
    }
   
def print_consumables():
    i = 1
    for item, details in playerStats.inventory.items():
        if details["type"] == "consumable":
            print(f"{i}. {item}({itemsInfo.healthDict[item]["amount"]} hp): {details['amount']}")    
            i += 1

def print_gold():
    print("You have " + str(playerStats.inventory["gold"]["amount"]) + " gold.")

def addXp(xpEarned):
    xpRequired = int(100 * (playerStats.level**1.5))
    playerStats.xp += xpEarned
    print("You earned " + str(playerStats.xp))
    while playerStats.xp >= xpRequired:
        playerStats.xp % xpRequired
        playerStats.level += 1
        print("You Leveled up! You are now level " + str(playerStats.level))
        playerStats.xp -= xpRequired
        xpRequired = int(100 * (playerStats.level**1.5))
        # playerStats.maximumHealth += 10
        playerStats.health = playerStats.maximumHealth

    print("current experience (" + str(playerStats.xp) + "/" + str(xpRequired) + ")")
    return xpRequired