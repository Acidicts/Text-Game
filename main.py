import random
import time
import os


global dp
global hp
global newws
global maxhp
global starter
global structures
global gold
global discovered
global gems
global market
global stuff
global lvl

discovered = []
newws = 0
lvl = 1
stuff = []
starter = True

def shop():
    print("What would you like?")
    print("[1] Weapons")
    print("[2] Armour")
    print("[3] Potions")
    print("[4] Spells")
    print("[5] Gems")
    print("[6] Containers")
    print("[7] Back")
    i = input(" ")
    if i == "7":
        home()
    options(i)

def options(c):
    global starter
    if c == "1":
        if starter == True:
            print("[1] Rusted Sword 0")
            print("[2] Stained Sword 20")
            print("[3] Stainless Steel Sword 40")
            print("[4] Blood-Slayer Sword 70")
            print("[5] Back")
            i = input(" ")
            if i == "1":
                starter = False
                itemShop("Rusted Sword", "0")
            elif i == "2":
                itemShop("Stained Sword", "20")
            elif i == "3":
                itemShop("Stainless Steel Sword", "40")
            elif i == "4":
                itemShop("Blood-Slayer", "70")
            elif i == "5":
                home()
            else:
                options(c)
        else:
            print("[1] Worn Sword 10")
            print("[2] Stained Sword 20")
            print("[3] Stainless Steel Sword 40")
            print("[4] Blood-Slayer Sword 70")
            i = input(" ")
            if i == "1":
                itemShop("Worn Sword", 10)
            elif i == "2":
                itemShop("Stained Sword", 20)
            elif i == "3":
                itemShop("Stainless Steel Sword", 40)
            elif i == "4":
                itemShop("Blood-Slayer", 70)
            elif i == "5":
                home()
            else:
                options(c)

    elif c == "2":
        print("[1] Old Armour 10")
        print("[2] Stained Armour 20")
        print("[3] Stainless Steel Armour 40")
        print("[4] Blood-Slayer Armour 70")
        i = input(" ")
        if i == "1":
            itemShop("Old Armour", 10)
        elif i == "2":
            itemShop("Stained Armour", 20)
        elif i == "3":
            itemShop("Stainless Steel Armour", 40)
        elif i == "4":
            itemShop("Blood-Slayer Armour", 70)
        elif i == "5":
            home()
        else:
            options(c)

    elif c == "3":
        print("[1] Weak-Health Potion 10")
        print("[2] Strong-Health Potion 20")
        print("[3] Double-Damage Potion 50")
        print("[4] Avatar Potion 1000")
        i = input(" ")
        if i == "1":
            itemShop("Weak-Health Potion", 10)
        elif i == "2":
            itemShop("Strong-Health Potion", 20)
        elif i == "3":
            itemShop("Double-Damage Potion", 50)
        elif i == "4":
            itemShop("Avatar Potion", 1000)
        elif i == "5":
            home()
        else:
            options(c)

    elif c == "4":
        print("[1] Fire-Ball 10")
        print("[2] Blizzard 20")
        print("[3] Acid-Rain 40")
        print("[4] Merlin's Wrath 100")
        i = input(" ")
        if i == "1":
            itemShop("Fire-Ball", 10)
        elif i == "2":
            itemShop("Blizzard", 20)
        elif i == "3":
            itemShop("Acid-Rain", 40)
        elif i == "4":
            itemShop("Merlin's Wrath", 100)
        elif i == "5":
            home()
        else:
            options(c)

    elif c == "5":
        print("[1] Unstable-Gem 10")
        print("[2] Cracked-Gem 20")
        print("[3] Unknown-Gem 40")
        print("[4] Gem-Of-Death 2000")
        i = input(" ")
        if i == "1":
            itemShop("Unstable-Gem", 10)
        elif i == "2":
            itemShop("Cracked-Gem", 20)
        elif i == "3":
            itemShop("Unknown-Gem", 40)
        elif i == "4":
            itemShop("Gem-Of-Death", 2000)
        elif i == "5":
            home()
        else:
            options(c)

    elif c == "6":
        print("[1] Gem Stablizer 1280")
        print("[2] Gem Paste 160")
        print("[3] Gem Harnesser 400")
        print("[4] Gem Reactivator 2000")
        i = input(" ")
        if i == "1":
            itemShop("Gem Stablilizer", 1280)
        elif i == "2":
            itemShop("Gem Paste", 160)
        elif i == "3":
            itemShop("Gem Harnesser", 400)
        elif i == "4":
            itemShop("Gem Reactivator", 2000)
        elif i == "5":
            home()
        else:
            options(c)

def itemShop(item, price):
    global gold
    print("You have {} gold".format(gold))
    print("Would you like to buy {} for {}".format(item, str(price)))
    print("Y/N")
    print(" ")
    int()
    i = input(" ")
    if i == "Y" or i == "y":
        if gold > int(price):
            gold -= int(price)
            stuff.append(item)
            shop()
        else:
            print("You don't have enough gold")
            time.sleep(1)
            shop()
    else:
        print("Too bad")
        shop()

def battlefield():
    global hp
    global dp
    global lvl
    global gold
    global stuff
    md = lvl * random.randint(10,40)
    mobs = ["Goblin", "Gargoyle", "Stone Golem", "Vampire", "Chimera", "Hydra"]
    mhp = lvl * random.randint(10,70)
    mob = random.randint(0, 3)
    m = mobs[mob]
    hp = 20
    weapons()

    while mhp > 0 and hp > 0:
        print("You Encounter a {}".format(m))
        print("It has {} hp".format(mhp))
        print("You have {} hp".format(hp))
        print("Your Damage is {}".format(dp))

        mhp, hp = attack(mhp, md)


    g = random.randint(0, 30)
    l = random.randint(1, 3)
    l = l/10
    lvl += l
    gold += g
    print("You defeated the beast")
    print("And you gained {} gold".format(g))
    print("You gained {} exp".format(l))
    print("You are now level {}".format(lvl))
    time.sleep(2)

    print(" ")
    print("Would you like to fight another monster? Y/N")
    i = input("")
    if i == "Y" or i == "y":
        print("You ran in to the battefield again")
        time.sleep(2)
        battlefield()

    home()

def dungeon():
    for i in range(random.randint(3,10)):
        global hp
        global dp
        global lvl
        global gold
        global stuff
        md = lvl * random.randint(10, 40)
        mobs = ["Goblin", "Gargoyle", "Stone Golem", "Vampire"]
        mhp = lvl * random.randint(10, 70)
        mob = random.randint(0, 3)
        m = mobs[mob]
        hp = 20
        weapons()

        while mhp > 0 and hp > 0:
            print("You Encounter a {}".format(m))
            print("It has {} hp".format(mhp))
            print("You have {} hp".format(hp))
            print("Your Damage is {}".format(dp))

            mhp, hp = attack(mhp, md)

        g = random.randint(0, 30)
        l = random.randint(1, 3)
        l = l / 10
        lvl += l
        gold += g
        print("You defeated the beast")
        print("And you gained {} gold".format(g))
        print("You gained {} exp".format(l))
        print("You are now level {}".format(lvl))
        time.sleep(2)

    structure, sn = dungeonStructure()

    print("You have found {}".format(structure))
    dungeonEnd(sn)

def attack(mhp, md):
    global dp
    global hp
    print("[1] Would you like to attack?")
    print("[2] Block")
    print("[3] Heal")
    print("[4] Slam")
    print("[5] Spell")
    print("[6] Run")
    i = input("")
    if i == "1":
        mhp -= dp
        hp -= md

    elif i == "2":
        pass

    elif i == "3":
        if "Weak Health Potion" in stuff:
            hp += 10
            stuff.remove("Weak Health potion")
        elif "Strong Health Potion" in stuff:
            hp += 30
            stuff.remove("Strong Health potion")

    elif i == "4":
        mhp -= dp

    elif i == '5':
        if "Fireball" in stuff:
            print("You have a Fireball spell would you like to use it y/n")
            n = input(" ")
            if n == "y":
                mhp -= 10
        elif "Blizzard" in stuff:
            print("You have a Blizzard spell would you like to use it y/n")
            n = input(" ")
            if n == "y":
                mhp -= 20
        elif "Acid Rain" in stuff:
            print("You have a Acid Rain spell would you like to use it y/n")
            n = input(" ")
            if n == "y":
                mhp -= 40
        elif "Merlin's Wrath" in stuff:
            print("You have a Merlin's Wrath spell would you like to use it y/n")
            n = input(" ")
            if n == "y":
                mhp -= 100

    elif i == "6":
        r = random.randint(0,3)
        if r == 0:
            print("You Safely Excaped")
            time.sleep(2)
            home()
        elif r == 1:
            print("You Safely Excaped")
            time.sleep(2)
            home()
        elif r == 2:
            print("You Safely Excaped")
            time.sleep(2)
            home()
        elif r == 3:
            print("You Failed Your Escape")
            for i in range(len(stuff)):
                stuff.remove(0)


    return mhp, hp

def dungeonStructure():
    bs = None
    bv = random.randint(0, 5)

    if bv == 0:
        bs = "Dwarven Cavern"
        bn = 0
    elif bv == 1:
        bs = "Forge of the Gods"
        bn = 1
    elif bv == 2:
        bs = "Ancient City"
        bn = 2
    elif bv == 3:
        bs = "Elven Tree"
        bn = 3
    elif bv == 4:
        bs = "Diamond Encrusted Chamber"
        bn = 4
    elif bv == 5:
        bs = "A lost Civilization"
        bn = 5
    return bs, bn

def dungeonEnd(sn):
    s = sn
    dn = None
    if s == 0:
        print("A Dwarf turns to examines you")
        dn = 0
    elif s == 1:
        print("The Forge Exhausts it's Heat")
        dn = 1
    elif s == 2:
        print("The Gloomy City Watches You")
        dn = 2
    elif s == 3:
        print("The Elven Tree Resonates with Magic")
        dn = 3
    elif s == 4:
        print("The Diamonds Hum in your Presence")
        dn = 4
    elif s == 5:
        print("The Civilians Scowl and hide")
        dn = 5

def dungeonActivity(d):
    def dwarvenCavern():
        print("The Dwarf took you to their leader")
        print("Who has disturbed my slumber?")
        print("You cowered in fear")
        print("You explain your presence")

def potions(hp,dm):
    if "Weak-Health Potion" in stuff:
        hp += 10
    if "Strong-Health Potion return" in stuff:
        hp += 20
    if "Double-Damage Potion" in  stuff:
        print("Would You like to use a Double-Damage Potion?")
        print("Y/N")
        i = input("")
        if i == "Y" or i == "y":
            dm *= 2
            stuff.remove(stuff.index("Double-Damage Potion"))
            print("Potion used")
        else:
            pass
    if "Avatar Potion" in stuff:
        print("Do you want to use the Avatar Potion?")
        print("Y/N")
        i = input("")
        if i == "Y" or i == "y":
            dm = 1000
            stuff.remove(stuff.index("Avatar Potion"))
            print("You feel the elements surge around you")

    print("Your have healed {}".format(hp))

    return hp, dm

def weapons():
    global dp
    dp = 0
    if "Rusted Sword" in stuff:
        dp += 10
    elif "Old Sword" in stuff:
        dp += 20
    elif "Stained Sword" in stuff:
        dp += 25
    elif "Stainless Steel Sword" in stuff:
        dp += 30
    elif "Blood-Slayer" in stuff:
        dp += 50


def gemForge():
    if "Unstable-Gem" in stuff and "Gem Stablizer" in stuff:
        print("Your Unstable Gem is Uncontrollably attaching to you Gem Stabilizer")
        stuff.remove("Unstable-Gem")
        stuff.remove("Gem Stablizer")
        stuff.append("Stable Staff")

    elif "Cracked-Gem" in stuff and "Gem Paste" in stuff:
        print("Your Gem Paste is When Applied Heals your Cracked Gem")
        stuff.remove("Cracked-Gem")
        stuff.remove("Gem Paste")
        stuff.append("Sealed Gem")

    elif "Unknown Gem" in stuff and "Gem Harnesser" in stuff:
        print("Your Unknown Gem Attaches itself to the Gem Harnesser and Releases a beam of light")
        stuff.remove("Unknown-Gem")
        stuff.remove("Gem Harnesser")
        stuff.append("Staff of Power")

    elif "Gem Reactivator" in stuff and "Gem-Of-Death" in stuff:
        print("Your Gem Reactivator is absorbed by your Gem-Of-Death")
        stuff.remove("Gem-Of-Death")
        stuff.remove("Gem Reactivator")
        stuff.append("Revived Gem of Death")

    else:
        print("You do not have a Gem or its item")
    home()

def inventory():
    global stuff
    global gold

    print("You Have:")
    print(str(gold))
    for i in range(len(stuff)):
        print(stuff[i])
        time.sleep(0.5)
    time.sleep(len(stuff))
    home()

def weaponShop():
    global newws
    if newws == 1:
        print("The Weapon-smith explains all the weapons he could make")
        print("But one catches your eye")
        print("The Sacred Blade of Asgard")
        print("Known to be owned by The God of Mischief himself")
        time.sleep(1)
        print("Loki")
        newws = 0

    print("[1] The Sacred Blade of Asgard")
    print("[2] The Unbreakable Blade")
    print("[3] Enchanted Sword of Death")
    print("[4] The Forever Living Staff")
    op = input(" ")
    if op == "1":
        print("The Blade was not forge here but in Asgard")
        print("This Blade has Unknown Properties")
        itemShop("The Sacred Blade of Asgard", 250)
    elif op == "2":
        print("Although Unbreakable not the strongest")
        print("Forged with Antimatter and Matter while neutralised")
        itemShop("The Unbreakable Blade", 200)
    elif op == "3":
        print("The Sword is the Gateway to the AfterLife")
        print("If it Falls into the Wrong Hands The souls Shall Haunt the World")
        itemShop("Enchanted Sword of Death", 400)
    elif op == "4":
        print("The Staff can live when you Die")
        print("The Dna infused with the staff could be the key to immortality")
        itemShop("The Forever Living Staff", 100)

def home():
    os.system("clear")
    global market
    global maxhp
    global hp
    global discovered
    if lvl == 10:
        market = True
    print("You can go to:")
    print("[1] To Bed")
    print("[2] Shop")
    print("[3] The Dungeon")
    print("[4] Dark Market")
    print("[5] Battlefield")
    print("[6] Inventory")
    print("[7] Gem Forge")
    print("[8] Explore")
    if "Weapon Shop" in discovered:
        print("[9] Weapon Shop")
    if "City" in discovered:
        print("[10] City")
    if "Armour Shop" in discovered:
        print("[11] Armour Shop")
    op = input(" ")


    if op == "1":
        print("Sleeping...")
        print("Your Heath is restored to {}".format(maxhp))
        hp = maxhp
        time.sleep(2)
        home()

    elif op == "2":
        print("Arriving at the shop")
        shop()

    elif op == "3":
        print("The Gates Felt Your Presence...")
        time.sleep(1)
        print("Creaking in the cool wind")
        dungeon()

    elif op == "4":
        print("Attempting access")
        if market == True:
            print("Success")
            market()
        else:
            print("Failed")
            home()

    elif op == "5":
        print("Calling General")
        time.sleep(random.randint(2,8))
        print("Accepted")
        battlefield()

    elif op == "6":
        print("Displaying in 3...")
        print("2..")
        print("1.")
        inventory()

    elif op == "7":
        print("Heating Gem Forge")
        time.sleep(3)
        gemForge()

    elif op == "8":
        global structures
        global newws
        en = random.randint(1,20)
        if en == 1:
            print(structures[0])
            discovered.append(structures[0])
            if structures[0] == "Weapon Shop":
                newws = 1
            structures.remove(structures[0])
            home()
            if len(structures) == 0:
                print("You have Discovered Everything")
        else:
            print("Failed")
            time.sleep(1)
            os.system("clear")
            home()


    elif op == "9":
        if "Weapon Shop" in discovered:
            print("The Weapon-Smith greets you")
            weaponShop()
        else:
            home()

    elif op == "10":
        if "City" in discovered:
            print("The City looms above you")
            weaponShop()
        else:
            home()

    elif op == "11":
        if "Armour Shop" in discovered:
            print("The Armourer greets you")
            weaponShop()
        else:
            home()

    else:
        home()

def start():
    global gold
    global structures
    global maxhp
    global market
    market = False
    structures = ["Weapon Shop", "City", "Armour Shop"]
    gold = random.randint(20,100)
    maxhp = random.randint(20,30)
    print("What is your name young adventurer")
    name = input(" ")
    print("Hello ", name, "You have ", gold, " gold")
    print("You have {} health".format(maxhp))
    print("To start I recommend using the shop to get some weapons and armour")
    home()

if __name__ == '__main__':
    start()
