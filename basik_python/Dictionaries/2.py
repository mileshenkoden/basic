enemy = {
    "loc_x": 70,
    "loc_y": 50,
    "color": "green",
    "heels": 100,
    "name": "mark",
    "image": ["imeg1.jpg,imeg2.jpg,imeg3.jpg"],
}

all_enemyes = []
for x in range(0, 10):
    all_enemyes.append(enemy)
for ene in all_enemyes:
    print(ene)


#print(all_enemyes)

