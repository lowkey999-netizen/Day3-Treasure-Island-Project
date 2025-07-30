print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
invalid_choice = "Invalid, start over."
way_choice = input("Your encounter a three way forked path\nLeft(l), Straight(s), and Right(r)\nWhich is your path?\nAnswer: ").lower()
if way_choice == "l":
    print("You step on a stray Demon King who was sleeping under the shade.\nDemon King: (ㆆ_ㆆ)\nThe Lamb that is going to get slaughtered(You): ʘ‿ʘ"
          "\nGood Job! You've angered Him.\n YOU DIED ")

elif way_choice == "s":
    s_path = input("You walk the golden brick road and arrive at the gates of a fabulous city of Rubies(NOT emeralds)."
                   "\n'WOW!' ╰༼ •̀۝•́ ༽╯ you squeal.\nEnter? 'y' for Yes, 'y' for Yes.\nAnswer: ").lower()
    if s_path == "y":
        final_path = input("BAM!! You realise that you entered a trap as the city turns into a Dragon's den. "
                           "Inside you find mountains of shiny things, on top of the center most area of the den you find "
                           "a small mound on which your goal lies in wait!\n The Treasure chest!\n Open it? 'y' for Yes, 'n' for No.\nAnswer: ").lower()
        if final_path == "y":
            crucial = input("A white dragon stops you from opening it.\n'k' to Slay it? or 'M' to Marry it?:")
            if crucial == "k":
                print("As expected of a peasant ಠ╭╮ಠ\n YOU DIED")
            elif crucial == "M":
                print("Congratulations!, the White dragon transforms into a beautiful white haired girl, and she accepts your proposal."
                      "\nNow you have gained both the treasure and something even more Precious\n A soulmate....\n -------THE END-------")
            else:
                print(invalid_choice)
        elif final_path == "n":
            print("You ignore it and grab a few gold coins from from a gold coin hill\nYou get cursed with explosive diarrhea\n YOU DIED")
        else:
            print(invalid_choice)
    else:
        print(invalid_choice)

elif way_choice == "r":
    print("May god have mercy on your soul because.........\nSURPRISE QUIZZZ!!!")
    r_path = input("Am I a handsome guy? Yes(y) or no(n)?\nAnswer: ").lower()
    if r_path == "n":
        print("Looks like you don't have any survival skills, not even an ounce of common sense.\n（╬￣皿￣）＝○＃（￣＃）３￣）\n RIP BOZO\n YOU DIED")
    elif r_path == "y":
        print("Humph! ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄  You're sensible!\n YOU SHALL PASS! ")
        r_path_ = input("Welcome to the abode of fairies! Do you wish to proceed and enjoy your life with pretty fairies from now on?"
                        "\n'y' for Yes, 'n' for No\nAnswer: ").lower()
        if r_path_ == "y" or r_path_ == "n":
            print("After passing my fabulous test, you arrive at a beautiful place full of pretty fairies and flowers."
                  "\nIn your 'own' bliss of passing my test, you failed to notice the portal *COUGH* *COUGH* that has appeared under you."
                  "\nWhat do you think has happened after that? :)\nThat's right! You......\nYOu..... \n \n YOu...\n \n YOU DIED ")
    else:
        print(invalid_choice)
else:
    print(invalid_choice)