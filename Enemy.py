#enemyStats[health][minimumDamage][maximumDamage][EnemyLevel][minCoins][maxCoins][maxspecdrop]
grasslandStats = [
    #Grass Lands
    [15, 3, 9, 1, 8, 18],  # Wild Boar (Level 1)
    [25, 7, 12, 3, 12, 25],  # Stray Wolf (Level 3)
    [40, 10, 15, 5, 18, 35],  # Giant Hornet (Level 5)
    [75, 12, 18, 7, 25, 50],  # Goblin Scout (Level 7)
    [100, 15, 20, 9, 35, 70],  # Bandit Ruffian (Level 9)
]

darkForestStats = [
    #Dark Forest
    [150, 18, 22, 11, 45, 90],  # Shadow Stalker (Level 11)
    [175, 20, 25, 13, 55, 110],  # Venomfang Spider (Level 13)
    [200, 22, 28, 15, 70, 130],  # Cursed Treant (Level 15)
    [225, 25, 30, 17, 85, 160],  # Wraith of the Woods (Level 17)
    [250, 28, 32, 19, 100, 200],  # Nightfang Wolf (Level 19)
]

frozenPeakStats = [
    #Frozen Peaks
    [275, 30, 35, 21, 120, 250],  # Frostbite Bear (Level 21)
    [300, 32, 38, 23, 140, 280],  # Ice Golem (Level 23)
    [325, 35, 40, 25, 160, 320],  # Snow Harpy (Level 25)
    [350, 38, 42, 27, 180, 370],  # Avalanche Beast (Level 27)
    [375, 40, 45, 29, 200, 420],  # Frost Wraith (Level 29)
]

lostCaveStats = [
    #Lost Caves
    [400, 42, 48, 31, 250, 500],  # Cave Dweller (Level 31)
    [425, 45, 50, 33, 280, 550],  # Stone Serpent (Level 33)
    [450, 48, 52, 35, 320, 600],  # Phantom Miner (Level 35)
    [475, 50, 55, 37, 350, 650],  # Undead Explorer (Level 37)
    [500, 52, 58, 39, 400, 700],  # Crystal Guardian (Level 39)
]

burningWastesStats = [
    #Burning Wastes
    [525, 55, 60, 41, 450, 900],  # Ashen Revenant (Level 41)
    [550, 58, 62, 43, 500, 1000],  # Flame Wyrm (Level 43)
    [575, 60, 65, 45, 600, 1200],  # Magma Golem (Level 45)
    [600, 62, 68, 47, 700, 1400],  # Infernal Hound (Level 47)
    [625, 65, 70, 49, 800, 1600]   # Blazing Demon (Level 49)
]

grasslandEnemies = [
    "Wild Boar (Level " + str(grasslandStats[0][3]) + ")",
    "Stray Wolf (Level " + str(grasslandStats[1][3]) + ")",
    "Giant Hornet (Level " + str(grasslandStats[2][3]) + ")",
    "Goblin Scout (Level " + str(grasslandStats[3][3]) + ")",
    "Bandit Ruffian (Level " + str(grasslandStats[4][3]) + ")"
]

darkForestEnemies = [
    "Shadow Stalker (Level " + str(darkForestStats[0][3]) + ")",
    "Venomfang Spider (Level " + str(darkForestStats[1][3]) + ")",
    "Cursed Treant (Level " + str(darkForestStats[2][3]) + ")",
    "Wraith of the Woods (Level " + str(darkForestStats[3][3]) + ")",
    "Nightfang Wolf (Level " + str(darkForestStats[4][3]) + ")"
]

frozenPeaksEnemies = [
    "Frostbite Bear (Level " + str(frozenPeakStats[0][3]) + ")",
    "Ice Golem (Level " + str(frozenPeakStats[1][3]) + ")",
    "Snow Harpy (Level " + str(frozenPeakStats[2][3]) + ")",
    "Avalanche Beast (Level " + str(frozenPeakStats[3][3]) + ")",
    "Frost Wraith (Level " + str(frozenPeakStats[4][3]) + ")"
]

lostCavesEnemies = [
    "Cave Dweller (Level " + str(lostCaveStats[0][3]) + ")",
    "Stone Serpent (Level " + str(lostCaveStats[1][3]) + ")",
    "Phantom Miner (Level " + str(lostCaveStats[2][3]) + ")",
    "Undead Explorer (Level " + str(lostCaveStats[3][3]) + ")",
    "Crystal Guardian (Level " + str(lostCaveStats[4][3]) + ")"
]

burningWastesEnemies = [
    "Ashen Revenant (Level " + str(burningWastesStats[0][3]) + ")",
    "Flame Wyrm (Level " + str(burningWastesStats[1][3]) + ")",
    "Magma Golem (Level " + str(burningWastesStats[2][3]) + ")",
    "Infernal Hound (Level " + str(burningWastesStats[3][3]) + ")",
    "Blazing Demon (Level " + str(burningWastesStats[4][3]) + ")"
]

def xpCalc(pLevel, eLevel):
    baseXp = 50 * (eLevel**1.2) 

    levelDiff = eLevel - pLevel
    print(f"Level difference: {levelDiff}")
    if levelDiff >= 3:
        xpMulti = 1 + (levelDiff - 2 * 0.25)
        if xpMulti > 2:
            xpMulti = 2
    elif levelDiff <= -3:
        xpMulti = 1 - (levelDiff + 2 * 0.25)
        print("HELLO")
        if xpMulti < 0.25:
            xpMulti = 0.1
    elif levelDiff <= 2 and levelDiff >= -2:
        xpMulti = 1

    xpEarned = int(baseXp * xpMulti)    
    return xpEarned