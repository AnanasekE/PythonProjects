import json


# template
# with open(r'C:\Users\janek\Desktop\the_vault-1.7.2p1.12.4\data\the_vault\loot_tables\chest\lvl0/gildedomega.json') as f:
#   data = json.load(f)
#
# g = open(r'C:\Users\janek\Desktop/jsontest.txt', 'w')
#
# for i in data["pools"][0]["entries"]:
#     # print(i["_name"])
#     print(i["_name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')
#     g.write(i["_name"] + '\n'+ 'weight: ' + str(i['weight']) + 2* '\n')
#
# g.close()


def lvl0():
    with open(
            r'C:\Users\janek\Desktop\the_vault-1.7.2p1.12.4\data\the_vault\loot_tables\chest\lvl0/gildedomega.json') as f:
        data = json.load(f)

    g = open(r'C:\Users\janek\Desktop/jsontest.txt', 'w')

    g.write('----------------------------------' + '\n' + 'Bonus pool: ' + 2 * '\n')
    print('Bonus Pool: ')

    for i in data["pools"][0]["entries"]:
        print(i["_name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')

        g.write(i["_name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')
    lightPoolEnd = '----------------------------------' + '\n' + 'Light Pool: ' + 2 * '\n'
    g.write(lightPoolEnd)
    print(lightPoolEnd)

    for j in data['pools'][1]['entries']:
        print(j["_name"] + '\n' + 'weight: ' + str(j['weight']) + 2 * '\n')

        g.write(j["_name"] + '\n' + 'weight: ' + str(j['weight']) + 2 * '\n')

    g.write('----------------------------------' + '\n' + 'Light Pool: ' + '\n')
    print('----------------------------------' + '\n' + 'Light Pool: ' + '\n')


def chestTesterGilded():
    lightPoolStart = '----------------------------------' + '\n' + 'Light Pool: ' + 2 * '\n'
    bonusPoolStart = '----------------------------------' + '\n' + 'Bonus pool: ' + 2 * '\n'

    g.write(bonusPoolStart)
    for i in data["pools"][0]["entries"]:
        try:
            g.write(i["_name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')
        except KeyError:
            g.write(i["name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')

    g.write(lightPoolStart)

    for j in data['pools'][1]['entries']:
        try:
            g.write(j["_name"] + '\n' + 'weight: ' + str(j['weight']) + 2 * '\n') or g.write(j['name'])
        except KeyError:
            g.write(j["name"] + '\n' + 'weight: ' + str(j['weight']) + 2 * '\n') or g.write(j['name'])

    g.write(bonusPoolStart)


def chestTesterNormal():
    trashPoolStart = '----------------------------------' + '\n' + 'Trash Pool: ' + 2 * '\n'
    resourcesPoolStart = '----------------------------------' + '\n' + 'Resources Pool: ' + 2 * '\n'
    powerupsPoolStart = '----------------------------------' + '\n' + 'Powerups Pool: ' + 2 * '\n'
    specialsPoolStart = '----------------------------------' + '\n' + 'Specials Pool: ' + 2 * '\n'

    g.write(trashPoolStart)
    for k in data["pools"][0]["entries"]:
        try:
            g.write(k["_name"] + '\n' + 'weight: ' + str(k['weight']) + 2 * '\n')
        except KeyError:
            g.write(k["name"] + '\n' + 'weight: ' + str(k['weight']) + 2 * '\n')

    g.write(resourcesPoolStart)
    for c in data["pools"][1]["entries"]:
        try:
            g.write(c["type"] + '\n' + 'weight: ' + str(c['weight']) + 2 * '\n')
        except KeyError:
            g.write(c["name"] + '\n' + 'weight: ' + str(c['weight']) + 2 * '\n')

    g.write(powerupsPoolStart)
    for w in data["pools"][2]["entries"]:
        try:
            g.write(w["type"] + '\n' + 'weight: ' + str(w['weight']) + 2 * '\n')
        except KeyError:
            g.write(w["name"] + '\n' + 'weight: ' + str(w['weight']) + 2 * '\n')

    try:
        g.write(specialsPoolStart)
        for e in data["pools"][3]["entries"]:
            try:
                g.write(e["name"] + '\n' + 'weight: ' + str(e['weight']) + 2 * '\n')
            except KeyError:
                g.write(e["type"] + '\n' + 'weight: ' + str(e['weight']) + 2 * '\n')
    except IndexError:
        pass


levels = [0, 25, 50, 75, 100, 150, 200, 250]
chType = ['gilded', 'normal']
rarities = ['common', 'rare', 'epic', 'omega']

for lvl in levels:
    for chestType in chType:
        if chestType == 'normal':
            chestType = 'vaultchest'
        for rarity in rarities:

            with open(
                    r'C:\Users\janek\Desktop\the_vault-1.7.2p1.12.4\data\the_vault\loot_tables\chest\lvl' + str(
                        lvl) + '/' + chestType + rarity + '.json') as f:
                data = json.load(f)

            g = open(r'C:\Users\janek\Desktop/jsontest.txt', 'w')

            if chestType == 'gilded':
                print(chestType, rarity, lvl)
                chestTesterGilded()
                print('end')
            else:
                print(chestType, rarity, lvl)
                chestTesterNormal()
                print('end')
g.close()
