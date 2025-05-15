import Enemy
import Player
import WorldMap
import combat   
import itemsInfo
import os

#Select the location you would like to travel to 
def traveling():
    print("Where would you like to travel to?")

    #Prints the list of places you can travel to 
    for i in range(0, len(WorldMap.locationsList)):
        print(str(i + 1) +  ". " + WorldMap.locationsList[i])
        i += 1

    #Prints you current location
    invalidResponse = True
    while invalidResponse:
        x = int(input())
        #Checks to see if your input is within range of the list of possible places to travel
        if x > 1 and x < len(WorldMap.locationsList) + 1:
            print("You are now in " + WorldMap.locationsList[x - 1])
            invalidResponse = False
            return x
        elif x == 1:
            print("You have opened your inventory")
            return x
        else:
            print("Invalid response please try again")

#Select the enemy that you want to fight based on your location 
def enemySelection(list, array):
    #print each of the enemies in the area
    for i in range(0, len(list)):
        print(str(i + 1) +  ". " + list[i])
        i += 1
    x = input()
    print(list[int(x) - 1])

    #Print player and enemy stats
    enemy_stats = array[int(x) - 1]
    print(f"Health: {enemy_stats[0]} \nMin Damage: {enemy_stats[1]} \nMax Damage: {enemy_stats[2]}")
    print()
    print("Player (Level " + str(Player.playerStats.level) + ") \nHealth: " + str(Player.playerStats.health) + " \nMin Damage: " + str(Player.playerStats.minimumDamage) + " \nMax Damage: " + str(Player.playerStats.maximumDamage))
    return enemy_stats

#Allows you to choose what enemy you want to fight depending on your location
def pickingEnemy(x):
    print("Pick an enemy to fight")
    if x == 3:
        enemyStats = enemySelection(Enemy.grasslandEnemies, Enemy.grasslandStats)
    elif x == 4:
        enemyStats = enemySelection(Enemy.darkForestEnemies, Enemy.darkForestStats)
    elif x == 5:
        enemyStats = enemySelection(Enemy.frozenPeaksEnemies, Enemy.frozenPeakStats)
    elif x == 6:
        enemyStats = enemySelection(Enemy.lostCavesEnemies, Enemy.lostCaveStats)
    elif x == 7:
        enemyStats = enemySelection(Enemy.burningWastesEnemies, Enemy.burningWastesStats)
    
    initialHealth = enemyStats[0]
    return enemyStats, initialHealth

#Fighting, Buffing, and Running is managed here
def combatSit(initialHealth):
    #While the enemy is not dead run the method
    while enemyStats[0] > 0:
        print("Attack, Buff, or Run? (a/b/r)")
        action = input()
        #Applies damage to the player and the enemy
        if action == "a":
            enemyDamage = combat.attack(enemyStats[1], enemyStats[2])
            playerDamage = combat.attack(Player.playerStats.minimumDamage, Player.playerStats.maximumDamage)

            enemyStats[0] -= playerDamage

            if enemyStats[0] <= 0:
                print("Enemy Health: 0")
                enemyDead = True
            else:
                Player.playerStats.health -= enemyDamage
                #When enemy is dead set enemyDead = true
                print("Player Health: " + str(Player.playerStats.health))
                print("Enemy Health: " + str(enemyStats[0]))
        elif action == "b":
            Player.print_consumables()

            x = int(input()) - 1

            if x == len(itemsInfo.healthPotions):
                return

            Player.playerStats.health += itemsInfo.healthPotions[x][1]
            Player.playerStats.inventory[itemsInfo.healthPotions[x][0]]["amount"] -= 1

            if Player.playerStats.health > Player.playerStats.maximumHealth:
                Player.playerStats.health = Player.playerStats.maximumHealth

            

            print("Player Health: " + str(Player.playerStats.health))
            print("Enemy Health: " + str(enemyStats[0]))
        elif action == "r":
            return
    enemyStats[0] = initialHealth
    #If the enemy is dead provide players with xp and roll drops
    if enemyDead:
        xpEarned = Enemy.xpCalc(Player.playerStats.level, enemyStats[3])
        xpRequired = Player.addXp(xpEarned)
        gold = combat.loot(enemyStats[4], enemyStats[5])
        Player.playerStats.inventory["gold"]["amount"] += gold
        print("The enemy dropped " + str(gold) + " gold")
        Player.print_gold()

#Handles your interaction/s with the sword smith
def swordSmith():
    print("For which area would you like to purchase a weapon?")
    #Print the world locations to choose from
    for i in range(2, len(WorldMap.locationsList)):
        print(str(i - 1) +  ". " + WorldMap.locationsList[i])
        i += 1
    x = int(input())
    if x == 1:
        y = itemsInfo.grasslandSwords
    elif x == 2:
        y = itemsInfo.darkForestSword
    elif x == 3:
        y = itemsInfo.frozenPeakSwords
    elif x == 4:
        y = itemsInfo.lostCaveSwords
    elif x == 5:
        y = itemsInfo.burningWasteSwords
    
    #Prints the list of swords you can buy based on the area you selected
    Player.print_gold()

    if y == itemsInfo.grasslandSwords:
        y.pop(0)
    for i in range(0, len(y)):
        print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][4]) + " gold")
        i += 1
    print(str(i + 1) + ". Return")
    
    #Checks to see if you can buy an item or not
    buyItem = int(input()) - 1
    if buyItem == len(y):
        return
    elif Player.playerStats.inventory["gold"]["amount"] >= y[buyItem][4]:
        Player.playerStats.inventory["gold"]["amount"] -= y[buyItem][4]

        # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
        Player.playerStats.inventory[str(y[buyItem][0])] = {
            **itemsInfo.SwordsDict.get(str(y[buyItem][0]), {}),
            "type": "sword"
        }

        print(str(Player.playerStats.inventory[str(y[buyItem][0])]))

        y.pop(buyItem)

        # Add information from the dictionary with the same name
        Player.print_gold()
    else:
        print("You do not have enough gold to purchase this item")

#Handles your interaction/s with the Amourments Dealer
def amourmentsDealer():
        print("For which area would you like to purchase your armour?")
        #Print the world locations to choose from
        for i in range(2, len(WorldMap.locationsList)):
            print(str(i - 1) +  ". " + WorldMap.locationsList[i])
            i += 1
        x = int(input())
        if x == 1:
            y = itemsInfo.grasslandArmour
        elif x == 2:
            y = itemsInfo.darkForestArmour
        elif x == 3:
            y = itemsInfo.frozenPeakArmour
        elif x == 4:
            y = itemsInfo.lostCavesArmour
        elif x == 5:
            y = itemsInfo.burningWasteArmour
        
        #Prints the list of swords you can buy based on the area you selected
        Player.print_gold()
        for i in range(0, len(y)):
            print(str(i + 1) + ". " + str(y[i][0]) + " Price: " + str(y[i][3]) + " gold")
            i += 1
        print(str(i + 1) + ". Return")
        
        #Checks to see if you can buy an item or not
        buyItem = int(input()) - 1
        if buyItem == len(y):
            return
        elif Player.playerStats.inventory["gold"]["amount"] >= y[buyItem][3]:
            Player.playerStats.inventory["gold"]["amount"] -= y[buyItem][3]

            # print(str(itemsInfo.ArmourDict["Leather vest"]["price"]))
            Player.playerStats.inventory[str(y[buyItem][0])] = {
                **itemsInfo.ArmourDict.get(str(y[buyItem][0]), {}),
                "type": "armour"
            }
            
            print(str(Player.playerStats.inventory[str(y[buyItem][0])]))

            y.pop(buyItem)

            Player.print_gold()
        else:
            print("You do not have enough gold to purchase this item")

#Handles your interaction/s with the Potion Brewer
def potionBrewer():
    
    # prints the amount of available gold that you have in your inventory
    Player.print_gold()
    # prints the full list of available health potions
    for i in range(0, len(itemsInfo.healthPotions)):
        print(str(i + 1) + ". " + str(itemsInfo.healthPotions[i][0]) + " Price: " + str(itemsInfo.healthPotions[i][2]) + " gold")
        i += 1

    print(str(i + 1) + ". Return")

    # selects the health potion that you want to buy
    buyItem = int(input()) - 1
    
    if buyItem == len(itemsInfo.healthPotions):
        return
    
    # asks how many health potions you want to buy
    print("How many " + str(itemsInfo.healthPotions[buyItem][0]) + " would you like to buy?")
    amount = int(input())

    # checks if you have enough gold to buy the health potions
    if Player.playerStats.inventory["gold"]["amount"] >= itemsInfo.healthPotions[buyItem][2] * amount:
        Player.playerStats.inventory["gold"]["amount"] -= itemsInfo.healthPotions[buyItem][2] * amount

        # adds the health potions to your inventory inventory[potionName] | prints remaining gold and number of available health potions
        Player.playerStats.inventory[str(itemsInfo.healthPotions[buyItem][0])]["amount"] += amount
        Player.print_gold() 
        print("You now have " + str(Player.playerStats.inventory[str(itemsInfo.healthPotions[buyItem][0])]["amount"]) + " " + str(itemsInfo.healthPotions[buyItem][0]) + "(s) in your inventory")
    else:
        print("You do not have enough gold to purchase this item")
        return

#Prints enemy stats and drop rates based on the enemies you've killed
def dictionary():
    print("Currently not available")

#Prints all player stats to the user
def playerStats():
    print(str(Player.playerStats.health) + "/" + str(Player.playerStats.maximumHealth) + " health")
    print("Weapon: " + Player.playerStats.weapon + " DPS: " + str(Player.playerStats.minimumDamage) + "->" + str(Player.playerStats.maximumDamage))
    print("Armour: " + Player.playerStats.armour + " Damage Reduction: " + str(Player.playerStats.damageReduction))
    print("Level " + str(Player.playerStats.level) + " " + str(Player.playerStats.xp) + "/" + str(int(100 * (Player.playerStats.level**1.5))) + "xp")
    input()

#Allows you to interact with the stuff in town
def town():
    Player.playerStats.health = Player.playerStats.maximumHealth
    print("Welcome to town! What would you like to do?")

    #Prints the list of things you can do in town
    for i in range(0, len(WorldMap.townList)):
        print(str(i + 1) +  ". " + WorldMap.townList[i])
        i += 1

    #Choose what activity you would like to do within town
    invalidResponse = True
    while invalidResponse:
        x = int(input())
        if x > 0 and x < len(WorldMap.townList) + 1:
            print("You are now speaking to the " + WorldMap.townList[x - 1])
            invalidResponse = False
        else:
            print("Invalid response please try again")

    #When talking to the sword smith choose which area you would like to purchase your weapon from 
    if x == 1:
        swordSmith()
    elif x == 2:
        amourmentsDealer()
    elif x == 3:
        potionBrewer()
    elif x == 4:
        dictionary()
    elif x == 5:
        playerStats()

#Displays all the items within your inventory
def openInventory():
    Player.print_inventory()
    print("Would you like to equip any gear? (y/n)")
    x = input()
    equipmentList = []
    i = 0
    if x == "y":
        print("weapon or armour? (w/a)")
        x = input()
        if x == "w":
            for item, details in Player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'sword':
                    print(f"{i} - {item}: Min DPS: {details[0].get('minDps', 'N/A')} Max DPS: {details[0].get('maxDps', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'sword':
                    print(f"{i} - {item}: Min DPS: {details.get('minDps', 'N/A')} Max DPS: {details.get('maxDps', 'N/A')}")
                i += 1  
                equipmentList.append(item)
            print("Which item would you like to equip?")
            Player.playerStats.inventory[Player.playerStats.weapon] = {
                **itemsInfo.SwordsDict.get(Player.playerStats.weapon, {}),
                "type": "sword"
            }
            x = int(input())
            item = equipmentList[x]
            if itemsInfo.SwordsDict[item]["levelReq"] > Player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                Player.playerStats.weapon = equipmentList[x]
                Player.playerStats.minimumDamage = itemsInfo.SwordsDict[equipmentList[x]]["minDps"]
                Player.playerStats.maximumDamage = itemsInfo.SwordsDict[equipmentList[x]]["maxDps"]
            
        elif x == "a":
            for item, details in Player.playerStats.inventory.items():
                if isinstance(details, list) and details[0].get('type') == 'armour':
                    print(f"{i} - {item}: Damage Reduction: {details[0].get('dmgRed', 'N/A')}")
                elif isinstance(details, dict) and details.get('type') == 'armour':
                    print(f"{i} - {item}: Damage Reduction: {details.get('dmgRed', 'N/A')}")
                i += 1
                equipmentList.append(item)
            print("Which item would you like to equip?")
            x = int(input())
            Player.playerStats.inventory[Player.playerStats.armour] = {
                **itemsInfo.ArmourDict.get(Player.playerStats.armour, {}),
                "type": "armour"
            }
            item = equipmentList[x]
            if itemsInfo.ArmourDict[item]["levelReq"] > Player.playerStats.level:
                print("You are not a high enough level to equip this item")
            else:
                Player.playerStats.armour = equipmentList[x]
                Player.playerStats.damageReduction = itemsInfo.ArmourDict[equipmentList[x]]["dmgRed"]
        else:
            print()
    else:
        return
    equipmentList.clear()
    i = 0


#forever loop so that the game never ends unless manually closed
while True:
    x = traveling()
    # os.system('cls' if os.name == 'nt' else 'clear')
    if x >= 3:
        enemyStats, initialHealth = pickingEnemy(x)
        combatSit(initialHealth) 
    elif x == 2:
        town()
    elif x == 1:
        openInventory()