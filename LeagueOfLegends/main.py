import pandas as pd
import numpy as np




csvData = pd.read_csv("champions.csv")
Champion = csvData['Champion Name'].to_numpy()
Role = csvData['Role'].to_numpy()
Health = csvData['Base Health'].to_numpy()
Mana = csvData['Base Mana'].to_numpy()
Armor = csvData['Base Armor'].to_numpy()
Damage = csvData['Base Attack Damage'].to_numpy()
Gold = csvData['Gold Efficiency'].to_numpy()





def StatsSearch(RoleArray):
    print("Do you want to be more specific and search for champions stats?")
    SpecificInput = input("Health, Mana, Armor, Damage, Gold: ")
    MaxOrMin = input("Max or Min: ")

    if SpecificInput == "Health":
        if MaxOrMin == "Max":
            sorted_indices = np.argsort(RoleArray[1])[::-1]
        elif MaxOrMin == "Min":
            sorted_indices = np.argsort(RoleArray[1])


    elif SpecificInput == "Mana":
            if MaxOrMin == "Max":
                sorted_indices = np.argsort(RoleArray[2])[::-1]
            elif MaxOrMin == "Min":
                sorted_indices = np.argsort(RoleArray[2])

    elif SpecificInput == "Armor":
            if MaxOrMin == "Max":
                sorted_indices = np.argsort(RoleArray[3])[::-1]
            elif MaxOrMin == "Min":
                sorted_indices = np.argsort(RoleArray[3])


    elif SpecificInput == "Damage":
            if MaxOrMin == "Max":
                sorted_indices = np.argsort(RoleArray[4])[::-1]
            elif MaxOrMin == "Min":
                sorted_indices = np.argsort(RoleArray[4])


    elif SpecificInput == "Gold":
            if MaxOrMin == "Max":
                sorted_indices = np.argsort(RoleArray[5])[::-1]
            elif MaxOrMin == "Min":
                sorted_indices = np.argsort(RoleArray[5])



    sorted_health = np.array(RoleArray[1])[sorted_indices]
    sorted_names = np.array(RoleArray[0])[sorted_indices]
    sorted_mana = np.array(RoleArray[2])[sorted_indices]
    sorted_armor = np.array(RoleArray[3])[sorted_indices]
    sorted_damage = np.array(RoleArray[4])[sorted_indices]
    sorted_gold = np.array(RoleArray[5])[sorted_indices]

       

    for i in range(len(RoleArray[0])):
        print("Champion: ", sorted_names[i])
        print("Health: ", sorted_health[i])
        print("Mana: ", sorted_mana[i])
        print("Armor: ", sorted_armor[i])
        print("Damage: ", sorted_damage[i])
        print("Gold: ", sorted_gold[i])
        print("\n")
        



def SortingFunc(UserInput):
    CurrentRoleSelection = []
    ChampionStatsName = []
    ChampionStatsHealth = []
    ChampionStatsMana = []
    ChampionStatsArmor = []
    ChampionStatsDamage = []
    ChampionStatsGold = []
    for i in range(len(Role)):
            if Role[i] == UserInput:
                print(Champion[i])
                print("Health: ", Health[i])
                print("Mana: ", Mana[i])
                print("Armor: ", Armor[i])
                print("Damage: ", Damage[i])
                print("Gold Efficiency: ", Gold[i])
                print("\n")
                ChampionStatsName.append(Champion[i])
                ChampionStatsHealth.append(Health[i])
                ChampionStatsMana.append(Mana[i])
                ChampionStatsArmor.append(Armor[i])
                ChampionStatsDamage.append(Damage[i])
                ChampionStatsGold.append(Gold[i])
    CurrentRoleSelection.append(ChampionStatsName)
    CurrentRoleSelection.append(ChampionStatsHealth)
    CurrentRoleSelection.append(ChampionStatsMana)
    CurrentRoleSelection.append(ChampionStatsArmor)
    CurrentRoleSelection.append(ChampionStatsDamage)
    CurrentRoleSelection.append(ChampionStatsGold)
    


    StatsSearch(CurrentRoleSelection)



                

def SearchChampion():
    Userinput = input("Enter Role (Top, Jungle, Mid, ADC, Support): ")
    SortingFunc(Userinput)



SearchChampion()





