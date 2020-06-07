from os import system, name 
from time import sleep
from random import randint

#_____Definitions_____

ORANGE = '\033[33m' #Orange Text
GREEN =  '\033[32m' # Green Text
RED = '\033[31m' # Red Text
BLUE = '\033[96m' #Blue Text
PURPLE = '\033[95m' #Purple Text
END = '\033[m' # reset to the defaults
  
#game properties
town = 1
game = 1
floor = 0
maxFloor = 0
encounter = 0

#charater propertys
lvl = 1
gold = 0
health = 50
class Item:
    def __init__(self, name, strength, type):
        self.name = name
        self.strength = strength
        self.type = type
        
inv = [
    Item("Rookie Sword", 10, 1),
    Item("Rookie Bow", 7, 6),
    Item("Rookie Armor", 10, 11),
    Item("Empty", 0, 0),
    Item("Empty", 0, 0),
    Item("Empty", 0, 0)
]
equipHands = Item("Empty", 0, 0)
equipHead = Item("Empty", 0, 0)
equipBody = Item("Empty", 0, 0)
selected = Item("Empty", 0, 0)
store = [
    Item("Empty", 0, 0),
    Item("Empty", 0, 0),
    Item("Empty", 0, 0),
    Item("Empty", 0, 0),
    Item("Empty", 0, 0),
    Item("Empty", 0, 0)
]
tp = []
#warning - he THICC
adjList = [
    'Defiant',
    'Adorable',
    'Delightful',
    'Homely',
    'Quaint',
    'Adventurous',
    'Depressed',
    'Horrible',
    'Aggressive',
    'Determined',
    'Hungry',
    'Real',
    'Difficult',
    'Repulsive',
    'Alive',
    'Ill',
    'Rich',
    'Amused',
    'Distinct',
    'Angry',
    'Disturbed',
    'Impossible',
    'Scary',
    'Dizzy',
    'Inexpensive',
    'Annoying',
    'Innocent',
    'Shiny',
    'Drab',
    'Shy',
    'Dull',
    'Itchy',
    'Silly',
    'Sleepy',
    'Attractive',
    'Eager',
    'Jealous',
    'Smiling',
    'Average',
    'Easy',
    'Jittery',
    'Awful',
    'Jolly',
    'Sore',
    'Elegant',
    'Sparkling',
    'Bad',
    'Splendid',
    'Beautiful',
    'Enchanting',
    'Kind',
    'Spotless',
    'Better',
    'Encouraging',
    'Stormy',
    'Energetic',
    'Lazy',
    'Strange',
    'Black',
    'Enthusiastic',
    'Light',
    'Stupid',
    'Bloody',
    'Envious',
    'Lively',
    'Successful',
    'Blue',
    'Evil',
    'Lonely',
    'Super',
    'Excited',
    'Long',
    'Blushing',
    'Expensive',
    'Lovely',
    'Talented',
    'Exuberant',
    'Lucky',
    'Tame',
    'Brave',
    'Fair',
    'Magnificent',
    'Breakable',
    'Faithful',
    'Terrible',
    'Bright',
    'Famous',
    'Modern',
    'Tasty',
    'Busy',
    'Fancy',
    'Motionless',
    'Thankful',
    'Fantastic',
    'Muddy',
    'Calm',
    'Fierce',
    'Mushy',
    'Thoughtless',
    'Careful',
    'Filthy',
    'Mysterious',
    'Tired',
    'Cautious',
    'Fine',
    'Tough',
    'Charming',
    'Foolish',
    'Nasty',
    'Troubled',
    'Cheerful',
    'Fragile',
    'Clean',
    'Frail',
    'Nervous',
    'Ugliest',
    'Clear',
    'Nice',
    'Ugly',
    'Clever',
    'Friendly',
    'Frightened',
    'Unsightly',
    'Clumsy',
    'Funny',
    'Obedient',
    'Unusual',
    'Colorful',
    'Obnoxious',
    'Upset',
    'Combative',
    'Gentle',
    'Odd',
    'Uptight',
    'Comfortable',
    'Gifted',
    'Old-fashioned',
    'Glamorous',
    'Condemned',
    'Gleaming',
    'Outrageous',
    'Victorious',
    'Confused',
    'Glorious',
    'Outstanding',
    'Cooperative',
    'Good',
    'Courageous',
    'Gorgeous',
    'Panicky',
    'Wandering',
    'Crazy',
    'Graceful',
    'Perfect',
    'Creepy',
    'Plain',
    'Wicked',
    'Grotesque',
    'Pleasant',
    'Cruel',
    'Wild',
    'Curious',
    'Poor',
    'Cute',
    'Powerful',
    'Happy',
    'Precious',
    'Dangerous',
    'Healthy',
    'Prickly',
    'Dark',
    'Helpful',
    'Dead',
    'Putrid',
    'Hilarious',
]

def pause():
    input("Press <ENTER> to return")
    
def clear(): 
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear') 
    
    if(town == 1):
        print(" __                   ___ ")
        print('|""|  ___    _   __  |"""|  __ ')
        print('|""| |"""|  |"| |""| |"""| |""|        _._ _')
        print('|""| |"""|  |"| |""| |"""| |""|       (__((_(')
        print('|""| |"""|  |"| |""| |"""| |""|      \'-:--:-.')
        print('""""""""""""""""""""""""""""""""~~~~~~"-----"~~~~')
    else:
        print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
        print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
        print("_|___|___|" + GREEN + "Health - " + str(health) + END + "|___|" + ORANGE + "Gold - " + str(gold) + END + "_|___|" + RED + "Floor - " + str(floor) + END + "_|___|___|___|___|")
        print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
        print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")

#inventory function
def inventory():
    clear()
    print("this is your inventory")
    print("Slot 1 --- " + inv[0].name)
    print("Slot 2 --- " + inv[1].name)
    print("Slot 3 --- " + inv[2].name)
    print("Slot 4 --- " + inv[3].name)
    print("Slot 5 --- " + inv[4].name)
    print("Slot 6 --- " + inv[5].name)
    print()
    
    print("Equiped in hands --- " + equipHands.name)
    print("Equiped on head  --- " + equipHead.name)
    print("Equiped on Body  --- " + equipBody.name)
    
    user = input(GREEN + "View, Compare, Scrap, Equip, Return -- ").lower()
    if (user == "view" or user == "compare" or user == "scrap" or user == "equip"):
        slot = input("Witch slot or where equiped? -- " + END).lower()
        print(END)

        if (slot != "1" and slot != "2" and slot != "3" and slot != "4" and slot != "5" and slot != "6" and slot != "head" and slot != "hand" and slot != "hands" and slot != "body"):
            print(RED + "Sorry, I dont understand "+'make sure to type the number of the slot, or where it is equiped as "head" "hands" or "body"' + END)
            sleep(3)
            inventory()

        #yes I know view is set up diffrent. I found a better way after I made it and i'm not fixing it.
        if (user == "view"):
            if (slot == "hand" or slot == "hands"):
                viewEQItem(equipHands)
            elif (slot == "body"):
                viewEQItem(equipBody)
            elif (slot == "head"):
                viewEQItem(equipHead)
            else: viewItem(slot)
        elif (user == "compare"):
            compare(slot)
        elif (user == "scrap"):
            scrap(slot)
        elif (user == "equip"):
            equipItem(slot)
        
    elif (user == "return"):
        print(END)
        sleep(1)
    else:
        print(RED + "please use one of the commands listed" + END)
        sleep(1.5)
        inventory()
    clear()

def viewItem(slot):
    slot = int(slot)-1
    clear()
    print(GREEN + "Title - " + inv[slot].name + END)
    print("Strength - " + str(inv[slot].strength))
    print(PURPLE)
    pause()
    print(END)
    inventory()
def viewEQItem(item):
    clear()
    print(GREEN + "Title - " + item.name + " EQUIPED" + END)
    print("Strength - " + str(item.strength))
    print(PURPLE)
    pause()
    print(END)
    inventory()
def compare(slot1):
    clear()
    print("Slot 1 --- " + inv[0].name)
    print("Slot 2 --- " + inv[1].name)
    print("Slot 3 --- " + inv[2].name)
    print("Slot 4 --- " + inv[3].name)
    print("Slot 5 --- " + inv[4].name)
    print("Slot 6 --- " + inv[5].name)
    print()
    
    print("Equiped in hands --- " + equipHands.name)
    print("Equiped on head  --- " + equipHead.name)
    print("Equiped on Body  --- " + equipBody.name)
    
    slot2 = input(GREEN + "Compare to what? -- " + END).lower()
    print(END)

    if (slot2 != "1" and slot2 != "2" and slot2 != "3" and slot2 != "4" and slot2 != "5" and slot2 != "6" and slot2 != "head" and slot2 != "hand" and slot2 != "hands" and slot2 != "body"):
        print(RED + "Sorry, I dont understand "+'make sure to type the number of the slot, or where it is equiped as "head" "hands" or "body"' + END)
        sleep(2)
        compare(slot1)
    if (slot2 == "1" or slot2 == "2" or slot2 == "3" or slot2 == "4" or slot2 == "5" or slot2 == "6"):   
        slot2 = inv[int(slot2)-1] 
    if (slot1 == "1" or slot1 == "2" or slot1 == "3" or slot1 == "4" or slot1 == "5" or slot1 == "6"):
        slot1 = inv[int(slot1)-1]
    if (slot1 == 'hand' or slot1 == 'hands'):
        slot1 = equipHands
    if (slot2 == 'hand' or slot2 == 'hands'):
        slot2 = equipHands
    if (slot1 == "head"):
        slot1 = equipHead
    if (slot2 == "head"):
        slot2 = equipHead
    if (slot1 == "body"):
        slot1 = equipBody
    if (slot2 == 'body'):
        slot2 = equipBody
    clear()
    print(GREEN + "Title - " + str(slot1.name) + "          Title - " + str(slot2.name) + END)
    print("Strength - " + str(slot1.strength) + "                Strength - " + str(slot2.strength))
    print(PURPLE)
    pause()
    print(END)
    inventory()
def scrap(item):
    global inv
    global equipHands
    global equipHead
    global equipBody
    global gold
    print("Are you sure? Y/N")
    confirm = input("--->> ").lower()
    if (confirm == "yes" or confirm == "y"):
        if (item == "hand" or item == "hands"):
            gold += equipHands.strength
            equipHands = Item("Empty", 0, 0)
        elif (item == "body"):
            gold += equipBody.strength
            equipBody = Item("Empty", 0, 0)
        elif (item == "head"):
            gold += equipHead.strength
            equipHead = Item("Empty", 0, 0)
        else:
            slot = int(item)-1
            gold += inv[slot].strength
            inv[slot] = Item("Empty", 0, 0)
    elif (confirm == "no" or confirm == "n"):
        print("")
    else:
        print("please type yes or no")
        sleep(1)
    inventory()
def equipItem(item):
    global inv
    global equipHands
    global equipHead
    global equipBody
    if (item == "hand" or item == "hands" or item == "body" or item == "head"):
        print(RED + "You can't equip something that is allready equiped" + END)
    else:
        slot = int(item)-1
        if (inv[slot].type == 0):
            print(RED + "You can't equip something that isn't there" + END)
        if (inv[slot].type == 1 or inv[slot].type == 2 or inv[slot].type == 3 or inv[slot].type == 4 or inv[slot].type == 5 or inv[slot].type == 6 or inv[slot].type == 7 or inv[slot].type == 8 or inv[slot].type == 9 or inv[slot].type == 10):
            equipHands, inv[slot] = inv[slot], equipHands
        if (inv[slot].type == 11 or inv[slot].type == 12 or inv[slot].type == 13 or inv[slot].type == 14 or inv[slot].type == 15):
            equipBody, inv[slot] = inv[slot], equipBody
        if (inv[slot].type == 16 or inv[slot].type == 17 or inv[slot].type == 18 or inv[slot].type == 19 or inv[slot].type == 20):
            equipHead, inv[slot] = inv[slot], equipHead

    inventory()

def help():
    clear()
    print(BLUE)
    if (town == 1):
        print('You are in town, it is safe here.')
        print('Type "I" to access inventory')
        print('Type "Shop" to go to the shop and spend your coin or sell your equipment for a great price!')
        print('Type "Onward" to enter the dungeon')
        if(len(tp) > 0):
            print('teleport to a floor you have been to before by typeing "TP".')
    else:
        print('Type "I" to access inventory')
        print('Type "Town" to return to town at any time. but it is a one way trip')
        print('There are teleports every 10 floors. but they can only be activated from the inside')
        print('Move forward by typeing "onward"')
        print('You can only move forward if you have completd all of the encounters for the area.')
    print(END)
    sleep(1)

#shop functions
def shop():
    clear()
    global gold
    global inv
    print("Welcome to the store! would you like to buy or sell today?")
    user = input(GREEN + "Buy, Sell, Return -- ").lower()
    print(END)
    if (user == "buy"):
        buy()
    elif (user == "sell"):
        sell()
    elif (user == "return"):
        print("")
    else:
        print(RED + "please use one of the commands listed" + END)
        sleep(1.5)
        shop()
    clear()

def sell():
    global gold
    global inv
    global equipHands
    global equipHead
    global equipBody
    clear()
    print("Slot 1 --- " + inv[0].name)
    print("Slot 2 --- " + inv[1].name)
    print("Slot 3 --- " + inv[2].name)
    print("Slot 4 --- " + inv[3].name)
    print("Slot 5 --- " + inv[4].name)
    print("Slot 6 --- " + inv[5].name)
    print()
    print("Equiped in hands --- " + equipHands.name)
    print("Equiped on head --- " + equipHead.name)
    print("Equiped on Body --- " + equipBody.name)
    
    slot = input(PURPLE + "Witch slot or where equiped? (return to go back) -- " + END).lower()
    if (slot != "1" and slot != "2" and slot != "3" and slot != "4" and slot != "5" and slot != "6" and slot != "head" and slot != "hand" and slot != "hands" and slot != "body" and slot != "return"):
        print(RED + "Sorry, I dont understand "+'make sure to type the number of the slot, or where it is equiped as "head" "hands" or "body"' + END)
        sleep(3)        
        sell()
    elif (slot != "return"):
        print("Are you sure? Y/N")
        confirm = input("--->> ").lower()
        if (confirm == "yes" or confirm == "y"):
            item = slot
            if (item == "hand" or item == "hands"):
                gold += equipHands.strength*2
                equipHands = Item("Empty", 0, 0)
            elif (item == "body"):
                gold += equipBody.strength*2
                equipBody = Item("Empty", 0, 0)
            elif (item == "head"):
                gold += equipHead.strength*2
                equipHead = Item("Empty", 0, 0)
            else:
                slot = int(item)-1
                gold += inv[slot].strength*2
                inv[slot] = Item("Empty", 0, 0)
        elif (confirm == "no" or confirm == "n"):
            print("")
        else:
            print("please type yes or no")
            sleep(1)
        sell()
def buy():
    global gold
    global inv
    clear()
    print("Here is what we have in stock.")
    print(ORANGE + "your gold -- " + str(gold) + END)
    print("1 -- " + store[0].name + "    strength -- " + str(store[0].strength) + ORANGE + "  Price -- " + str(round(store[0].strength*3.2)) + END)
    print("2 -- " + store[1].name + "    strength -- " + str(store[1].strength) + ORANGE + "  Price -- " + str(round(store[1].strength*3.2)) + END)
    print("3 -- " + store[2].name + "    strength -- " + str(store[2].strength) + ORANGE + "  Price -- " + str(round(store[2].strength*3.2)) + END)
    print("4 -- " + store[3].name + "    strength -- " + str(store[3].strength) + ORANGE + "  Price -- " + str(round(store[3].strength*3.2)) + END)
    print("5 -- " + store[4].name + "    strength -- " + str(store[4].strength) + ORANGE + "  Price -- " + str(round(store[4].strength*3.2)) + END)
    print("6 -- " + store[5].name + "    strength -- " + str(store[5].strength) + ORANGE + "  Price -- " + str(round(store[5].strength*3.2)) + END)

    item = input(PURPLE + "Witch item to buy? (return to go back) -- " + END).lower()
    if (item != "1" and item != "2" and item != "3" and item != "4" and item != "5" and item != "6" and item != "return"):
        print(RED + "Sorry, I don't understand, "+'make sure to type the number of the item.' + END)
        sleep(3)        
        buy()
    elif (item != "return"):
        print("Are you sure? Y/N")
        confirm = input("--->> ").lower()
        if (confirm == "yes" or confirm == "y"):
            slot = findOpen()
            if(slot == 6):
                print(RED + "Sorry, but you don't have any free inventory to buy that" + END)
                sleep(2)
            else:
                if(gold >= round(store[int(item)-1].strength*3.2)):
                    gold -= round(store[int(item)-1].strength*3.2)
                    inv[slot], store[int(item)-1] = store[int(item)-1], inv[slot]
                else:
                    print(RED + "Sorry, but you don't have enough gold for that" + END)
                    sleep(2)
        elif (confirm == "no" or confirm == "n"):
            print("")
        else:
            print("please type yes or no")
            sleep(1)
        buy()

#item functions
def findOpen():
    global inv
    x = 0
    slot = 6
    for x in range(6):
        if ((inv[x].type) == 0):
            slot = x
            break
    return slot
    
def mkItem():
    adj = randint(0, len(adjList))
    typenum = randint(1, 20)
    if(typenum == 1):
        type = " Sword"
    elif(typenum == 2):
        type = " Longsword"
    elif(typenum == 3):
        type = " Spear"
    elif(typenum == 4):
        type = " Scyth"
    elif(typenum == 5):
        type = " Nunchuks"
    elif(typenum == 6):
        type = " Bow"
    elif(typenum == 7):
        type = " Longbow"
    elif(typenum == 8):
        type = " Crossbow"
    elif(typenum == 9):
        type = " Gun"
    elif(typenum == 10):
        type = " Slingshot"
    elif(typenum == 11):
        type = " Light Armor"
    elif(typenum == 12):
        type = " Heavy Armor"
    elif(typenum == 13):
        type = " Chainmail"
    elif(typenum == 14):
        type = " Leather Armor"
    elif(typenum == 15):
        type = " Platemail"
    elif(typenum == 16):
        type = " Helmet"
    elif(typenum == 17):
        type = " Hat"
    elif(typenum == 18):
        type = " Cap"
    elif(typenum == 19):
        type = " Mask"
    elif(typenum == 20):
        type = " Headware"
    name = adjList[adj] + type
    strength = randint(7*lvl, 12*lvl)
    return Item(name, strength, typenum)
def mkStore():
    x = 0
    for x in range(6):
        store[x] = mkItem()
mkStore()

def newRoom():
    global encounter
    global maxFloor
    global floor
    global lvl
    floor = floor+1
    clear()
    if(floor > maxFloor):
        maxFloor = floor
        if(maxFloor % 6 == 0):
            lvl += 1
        if(maxFloor % 10 == 0):
            tp.append(str(maxFloor))
            print(BLUE + "You found a teleporter on this floor!" + END)

    print("Welcome to floor " + str(floor) + ". You are on level " + str(lvl) + ".")
    enc = randint(0,10)
    if (enc <= 7):
        encounter = 1
        print(RED)
        print("you ran into a monster")
        print(END)
    sleep(1)
    

#icoperate death
def battle():
    global encounter
    global gold
    global inv
    global health
    clear()
    deff = equipBody.strength + equipHead.strength
    monDeff = randint(5*lvl, 9*lvl)
    monHealth = 20
    startHealth = health
    monster = 1

    while(monster == 1):
        atk = equipHands.strength
        luck = randint(1,10)
        if(luck == 1):
            atk = 0
            print(RED + "Miss" + END)
        elif(luck == 10):
            atk = atk*2
            print(GREEN + "Critical hit" + END)
        print("you attacked with " + str(atk) + " Damage.")
        print("The monster blocked " + str(monDeff) + " Damage.")
        cng = atk - monDeff
        if(cng > 0):
            monHealth -= cng
        print(GREEN + "Your health: " + str(health) + RED + "     Monster health: " + str(monHealth) + END)
        sleep(0.3)
        if(monHealth <= 0):
            monster = 0
            break

        monAtk = randint(10*lvl, 16*lvl)
        monLuck = randint(1,10)
        if(monLuck == 1):
            monAtk = 0
            print(GREEN + "The monster missed" + END)
        elif(monLuck == 10):
            monAtk = monAtk*2
            print(RED + "The monster got a critical hit" + END)
        print("The monster attacked with " + str(monAtk) + " Damage.")
        print("you blocked " + str(deff) + " Damage.")
        cng = monAtk - deff
        if(cng > 0):
            health -= cng
        print(GREEN + "Your health: " + str(health) + RED + "      Monster health: " + str(monHealth) + END)
        sleep(0.3)
        if(health <= 0):
            break
        if(monHealth == 20 and health == startHealth):
            monster = 3
            break
    clear()
    print(GREEN + "Your health: " + str(health))
    if(monster == 0):
        encounter += -1
        print(GREEN + "YOU WIN" + END)
        gold += round(monDeff/2)
        print("you found an item, Pick it up?")
        check = 0
        while(check == 0):
            confirm = input("--->> ").lower()
            if (confirm == "yes" or confirm == "y"):
                check = 1
                slot = findOpen()
                if(slot == 6):
                    print(RED + "Sorry, but you don't have any free inventory to pick it up" + END)
                    sleep(2)
                    clear()
                else:
                    inv[slot] = mkItem()
                    clear()
            elif (confirm == "no" or confirm == "n"):
                print("")
                check = 1
            else:
                print(RED + "please type yes or no" + END)
                sleep(1)
        
        sleep(1)
    elif(monster == 1):
        print(RED + "YOU DIED" + END)
        print("Better hobble to the portal back to town.")
    elif(monster == 3):
        encounter += -1
        print(RED + "Locked in combat, neither of you could do any damage" + END)
    
#_______logic_________
clear()
while game == 1:
    #in town
    if (town == 1):
        health = 50
        print(ORANGE + "Gold - " +str(gold) + RED + "  Max Depth - " + str(maxFloor) + END)
        print(GREEN)
        user = input("--->>").lower()
        print(END)

        if (user == "i"):
            inventory()
        elif (user == "onward" or user == "onwards"):
            town = 0
            newRoom()
        elif (user == "shop"):
            shop()
        elif (user == "tp"):
            if(len(tp)==0):
                print(RED + "none of the teleporters on on yet, try going deeper into the dungeon." + END)
                sleep(2)
                clear()
            else:
                print("what floor would you like to teleport to?")
                x=0
                print(BLUE)
                for x in range(len(tp)):
                    print("Floor - " + str(tp[x]))
                print(GREEN)
                user = input("--->>").lower()
                print(END)
                if (user == "return"):
                    clear()
                elif(str(user) in tp):
                    town = 0
                    floor = int(user)-1
                    newRoom()
                else:
                    print(RED + 'invalid option, type "help" for options' + END)
                    sleep(2)
                    clear()
        elif (user == "help"):
            help()
        elif (user == "exit" or user == "quit"):
            print(RED)
            print("exiting...")
            print(END)
            sleep(2)
            game = 0
        else:
            print(RED + 'invalid option, type "help" for options' + END)
            sleep(2)
            clear()


    #in dungeon
    while town == 0:
        print("Encounters - " + str(encounter))
        print(GREEN)
        user = input("--->>").lower()
        print(END)
        
        if (user == "i"):
            inventory()
        elif (user == "onward" or user == "onwards"):
            if (encounter == 0):
                newRoom()
            else:
                print(RED + "you cant leave a room until you finish all encounters" + END)
                sleep(2)
                clear()
        elif (user == "fight" or user == "battle"):
            if (encounter >= 1):
                battle()
            else:
                print(RED + "you can't fight something that's not there" + END)
                sleep(1)
                clear()
                
        elif (user == "help"):
            help()
        elif (user == "town"):
            print("Are you sure you want to return to town? it is a one way portal. Y/N")
            confirm = input("--->> ").lower()
            if (confirm == "yes" or confirm == "y"):
                town = 1
                mkStore()
                encounter = 0
                floor = 0
                clear()
            elif (confirm == "no" or confirm == "n"):
                clear()
            else:
                print("please type yes or no")
                sleep(1)
        else:
            print(RED + 'invalid option, type "help" for options' + END)
            sleep(2)
            clear()

