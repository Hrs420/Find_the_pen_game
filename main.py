print('''
**********************************************************
 ________________________________________________
 /\______________________________________________/`-.
<()>____________________________________________<    ##
 \/______________________________________________\,-'

*********************************************************
\n\n \n \n''')
print("Welcome to Find the Pencil Game. \n")
print("Your mission is to find the Pencil. \n\n")

print("Your Pencil has Lost! What you will do for your homework? ")

search = input(
    "You will search in your room  \n or Search in Arpit's Room ? (my,arpit)  "
)

if search.lower() == "arpit":
    ask = input(
        "They Were Doing S** You Wanna Disturb them or Go Down to find your pencil? (Disturb or down) \n\n"
    )
    if ask.lower() == "down":
        ask_2 = input(
            "You Wanna ask From Aditym , Aunty , Go and purchanse a new Pencil? (Aditym or Aunty or shop )\n\n"
        )
        if ask_2.lower() == "aditym":
            print(" MC Wo to nashe me hai . Game Over.\n\n")
        elif ask_2.lower() == "aunty":
            print(
                "Beta! Bijli ka bill dedo !! GAME OVER Now you will started talking to her!\n\n"
            )
        elif ask_2.lower() == "shop":
            print("Ye hui na Baat BC ! YOU WINN ! \n\n")
        else:
            print("Bsdk! Jitna pucha jaye to javab de !\n\n")

    else:
        print("you Lost! as they have Attacked you And Fu**ed You Also ! \n\n")
else:
    print("Nothing is there and you Lost! As you Don't have time Left \n\n")
