import random  # voor het raadspel
import time  # importeerd de tijd module om de tekt te vertragen

# Keuze opties voor de gebruiker
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "ja", "j"]
no = ["N", "n", "no", "nee", "no"]

required = ("\nError: Kies A of B \n")  # wanneer een verkeerde optie gekozen word
gold = 0  # werkt nog niet naar behoren, uitzoeken waarom!
sword = 0


# introductie van het spel
def intro():
    print("Hallo avonturier. Je zult getest worden op je heldhaftigheid, logica en geluk!")
    time.sleep(1)
    print("Wat is je naam? ")
    time.sleep(1)
    player_name = input(">>>")  # naamvandeheld  NOG NAAR ABC ONLY ZETTEN en definen zodat ie vaker te gebruiken is
    time.sleep(1)
    print(f"Hoi {player_name}... Ben je er klaar voor? ")
    pick_a_door()


def pick_a_door():
    print("Je wordt wakker in een donkere kamer.. Hoe kom ik hier? "
          "Voor je zie je een rode (A) en een blauwe (B) deur. "
          "Welke maak je open? ")
    choice = input(">>> ")
    if choice in answer_A:
        red_door()
    elif choice in answer_B:
        blue_door()
    else:
        print(required)
        intro()


def blue_door():
    print("\nThe blue door seems to be locked.. ")
    time.sleep(1)
    pick_a_door()


def red_door():
    print("Je opent de rode deur... ")
    time.sleep(1)

    print(r"""\
                     ___====-_  _-====___
               _--^^^#####//      \\#####^^^--_
            _-^##########// (    ) \\##########^-_
           -############//  |\^^/|  \\############-
         _/############//   (@::@)   \\############\_
        /#############((     \\//     ))#############\
       -###############\\    (oo)    //###############-
      -#################\\  / VV \  //#################-
     -###################\\/      \//###################-
    _#/|##########/\######(   /\   )######/\##########|\#_
    |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
    `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
       `   `  `      `   / | |  | | \   '      '  '   '
                        (  | |  | |  )
                       __\ | |  | | /__
                      (vvv(VVV)(VVV)vvv) """)
    print("Een DRAAK Wat doe je? Rol je van angst in een hoekje (A) of kies je er voor om te vechten (B)")
    choice = input(">>> ")
    if choice in answer_A:
        print("U DIE. Druk op A om het spel opnieuw te beginnen")
        choice = input(">>> ")
        if choice in answer_A:
            intro()


    elif choice in answer_B:
        gold = 1
        print(f"GEWONNEN! je vind een blauwe sleutel.")
        time.sleep(1)
    else:
        required
    blue_door_key()


def blue_door_key():
    print(
        "Met de mysterieuze blauwe sleutel in je hand ga je terug naar de vorige kamer. Druk op A om de sleutel in de blauwe deur te stoppen ")
    choice = input(" >>>")
    if choice in answer_A:
        print("""in de blauwe kamer tref je een slinkse Sphinx aan. 
              Als je zijn raadsels kunt oplossen laat hij je door naar de volgende ruimte!""")

        time.sleep(1)
        blue_room()
    else:
        blue_door_key()


def blue_room():
    time.sleep(1)
    print("Hier komen de raadsels")
    time.sleep(1)
    raadsel_1()


def raadsel_1():  # nog toevoegen hoe vaak raden en wat voor invloed dat heeft op monyez
    print("""First think of the person who lives in disguise,

Who deals in secrets and tells naught but lies.

Next, tell me what’s always the last thing to mend,

The middle of middle and end of the end?

And finally give me the sound often heard

During the search for a hard -to-find word.

Now string them together, and answer me this,

Which creature would you be unwilling to kiss?""")
    choice = input(">>>")
    if choice == "spider" or "spin":
        gold = + 1
        print(
            f"Slimmerik. Het antwoord is idd {choice}. Je hebt nu {gold} goudstukken. ")
        raadsel_2()
    else:
        print("Try again")
        raadsel_1()


def raadsel_2():
    print("""I have cities, but no houses. I have mountains, but no trees. 
    I have water, but no fish. What am I? """)
    choice = input(">>>")
    if choice == "2":
        print(f" Het antwoord is idd {choice}. Je hebt nu {gold + 1} goudstukken.")
        dobbelsteen()
    else:
        print("Try again")
        raadsel_2()


def dobbelsteen():
    min = 1
    max = 6

    print(r""" 

        ~'~,
       ~' *  ~,
    ,~' *    * ~,
    .~,*    *  ,~ :
    :  ~, *  ,~   :
    : *  ~,,~  *  :
    :* * * :  *   :
     ~, *  : *  ,~
       ~,  :  ,~
         ~,:,~
    """)
    time.sleep(1)

    print("You find a mysterious glowing dice. To roll press A")
    roll = 'a'
    roll = input(">>>")
    while roll == 'a' or roll == 'A':
        print("Je gooit de dobbel steen...")
        print("De dobbelsteen komt tot stilstand op....")
        uitkomst = (random.randint(min, max))
        time.sleep(1)
        print(f" het cijfer {uitkomst}")
        break
    else:
        dobbelsteen()

    aantal_keer_raden = uitkomst
    print(f"je mag {uitkomst} keer raden")
    time.sleep(1)

    random_number = random.randint(1, 10)
    while uitkomst <= 6:
        print("Kies een getal tussen 1 en 10")

        raden = int(input(">>>"))
        uitkomst -= 1
        if raden < random_number and uitkomst > 0:
            print("Te laag, probeer opnieuw")
        elif raden > random_number and uitkomst > 0:
            print("Te hoog, probeer opnieuw")
        elif raden == random_number or uitkomst == 0:
            break
    if uitkomst == 0:
        print(f"Helaas geen goud verdiend."
              f" het nummer was {random_number}")
    if raden == random_number:
        print(f'Goed gedaan. Je hebt {random_number} geraden. Dit klopt'
              f'Je hebt {uitkomst} keer raden nodig- gehad je mag de grot uit!')


intro()
