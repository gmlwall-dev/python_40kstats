import json
import time
import random
import inquirer

# read JSON data file
with open("data.json", "r") as file:
    data = json.load(file)

# number of simulations to run
iterations = 100000

# main script function selection
operations = ["melee simulator", "shooting simulator", "charge simulator"]

# function :: charge simulation
def simulation_charge(req_charge):
    success = []
    start = time.time()

    for i in range(iterations):
        roll = (random.randint(1, 6) + random.randint(1, 6))
        if roll >= req_charge:
            success.append(0)

    percent = (len(success) / iterations * 100)
    end = time.time()
    print("Based on", iterations, "simulations, you have a", percent, "% chance for success")
    print("This operation took:", end - start)

# function :: melee simulation
def simulation_melee_attack(faction_attacker, unit_attacker, faction_defender, unit_defender):
    success_tohit = []
    start = time.time()
    req_tohit = data[faction_attacker][unit_attacker]["Ws"]
    number_attacks = data[faction_attacker][unit_attacker]["A"]

    # generate attackers offense
    for i in range(iterations):
        for j in range(number_attacks):
            roll = (random.randint(1, 6))
            if roll >= req_tohit:
                success_tohit.append(0)

    T = data[faction_defender][unit_defender]["T"]
    W = data[faction_defender][unit_defender]["W"]
    S = data[faction_attacker][unit_attacker]["S"]
    Sv = data[faction_defender][unit_defender]["Sv"]

    # generate to wound roll
    if (T / S) >= 2:
        to_wound = 6
    elif (S / T) >= 2:
        to_wound = 2
    elif S < T:
        to_wound = 5
    elif S == T:
        to_wound = 4
    elif S > T:
        to_wound = 3

    # simulate to wound rolls
    success_towound = []
    for i in range(len(success_tohit)):
        roll = random.randint(1, 6)
        if roll >= to_wound:
            success_towound.append(0)

    # simulate save rolls
    success_tosave = []
    for i in range(len(success_towound)):
        roll = random.randint(1, 6)
        if roll >= Sv:
            success_tosave.append(0)

    # divide simulation results by no. iterations for average
    avg_tohit = len(success_tohit) / iterations
    avg_towound = len(success_towound) / iterations
    avg_saves = len(success_tosave) / iterations

    end = time.time()

    # print out stats
    print("Based on", iterations, "simulations:")
    print("Average hits =", avg_tohit)
    print("Average wounds =", avg_towound)
    print("Average saves =", avg_saves)
    print("Average damage = ", avg_towound - avg_saves)
    print("This operation took:", end - start)

# function :: unit selection
def unit_selection():
    faction_select = []
    for key in sorted(data.keys()):
        faction_select.append(key)

    q_faction = [
        inquirer.List('faction',
                      message="Select a faction",
                      choices=faction_select,
                      ),
    ]

    a_faction = inquirer.prompt(q_faction)

    unit_select = []
    for key in sorted(data[a_faction["faction"]].keys()):
        unit_select.append(key)

    q_unit = [
        inquirer.List('unit',
                      message="Select a unit",
                      choices=unit_select,
                      ),
    ]

    a_unit = inquirer.prompt(q_unit)
    return a_faction, a_unit

# menu for selections
q_operation = [
    inquirer.List('operations',
                  message="Select an operation",
                  choices=operations,
              ),
]

# store selection
a_operation = inquirer.prompt(q_operation)

# call function based on menu choice
if a_operation["operations"] == "charge simulator":
    print("enter the range required for successful charge")
    req_charge = int(input())
    simulation_charge(req_charge)

elif a_operation["operations"] == "melee simulator":
    print("Select attacking unit")
    result_attacker = unit_selection()
    faction, unit = result_attacker
    faction_attacker = faction["faction"]
    unit_attacker = unit["unit"]
    print("Select defending unit")
    result_defender = unit_selection()
    faction, unit = result_defender
    faction_defender = faction["faction"]
    unit_defender = unit["unit"]
    simulation_melee_attack(faction_attacker, unit_attacker, faction_defender, unit_defender)

elif a_operation["operations"] == "shooting simulator":
    print("shooting simulation selected")