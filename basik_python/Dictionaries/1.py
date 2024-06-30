enemy = {
    "loc_x": 70,
    "loc_y": 50,
    "color": "green",
    "heels": 100,
    "name": "mark"
}

#print("Locaition X = "+str(enemy["loc_x"]))
#print("Locaition Y =",enemy["loc_y"])

#enemy["reng"] = "coc"
#print(enemy)
#del(enemy["loc_y"])
#print(enemy)

enemy["loc_x"] = enemy["loc_x"] - 30
enemy["heels"] = enemy["heels"] - 25
if enemy["heels"] <= 80:
    enemy["color"] = "yelow"
print(enemy)
print(enemy.keys())
print(enemy.values())