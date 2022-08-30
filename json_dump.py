import json

# Data to be written
data = {
    "Harlequins" : {
        "Troupe Master" : {
            "Mv" : 8,
            "Ws" : 2,
            "Bs" : 2,
            "Ld" : 9,
            "Sv" : 6,
            "In" : 4,
            "S" : 3,
            "T" : 3,
            "W" : 5,
            "A" : 6
        },
        "Troupe" : {
            "Mv": 8,
            "Ws": 3,
            "Bs": 3,
            "Ld": 8,
            "Sv": 6,
            "In": 4,
            "S": 3,
            "T": 3,
            "W": 5,
            "A": 4
        }

    },
    "Death Guard" : {
        "Chaos Lord" : {
            "Mv": 6,
            "Ws": 2,
            "Bs": 2,
            "Ld": 9,
            "Sv": 3,
            "In": 4,
            "S": 4,
            "T": 5,
            "W": 5,
            "A": 5
        },
        "Plague Marine" : {
            "Mv": 5,
            "Ws": 3,
            "Bs": 3,
            "Ld": 7,
            "Sv": 3,
            "In": 0,
            "S": 4,
            "T": 5,
            "W": 2,
            "A": 2
        }
    }
    }


# Serializing JSON
json_object = json.dumps(data, indent=3)

# Writing to data.json
with open("data.json", "w") as outfile:
    outfile.write(json_object)