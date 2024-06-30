import json

file_name = "my_json_file"

my_file = open(file_name, mode="w", encoding="utf-8")

player_1 = {
    "name": "Daria",
    "speed":200,
    "awards": ["math","physic"]
}
player_2 = {
    "name": "Fare",
    "speed":220,
    "awards": ["lllf;.","physfgic"]
}
myplayers = []
myplayers.append(player_1)
myplayers.append(player_2)

"""---------------------SAVE by JSON------------------------"""

json.dump(myplayers,my_file)


my_file.close()
"""------------------------LOAD by LSON------------------"""

my_file = open(file_name, mode="r", encoding="utf-8")

json_date = json.load(my_file)

for user in json_date:
    print("Player name is " + str(user["name"]))
    print("Player speed is " + str(user["speed"]))
    print("Player awards is " + str(user["awards"][0]))
    print("Player awards is " + str(user["awards"][1]))
    print("---------------------------\n\n")