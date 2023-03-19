# weight = int(input("BMI calculator beach!\nWrite your weight here pig: "))
# height = int(input("Now write ur height in cm: "))
#
# bmi = weight / (height / 100) ** 2
#
# if bmi < 18.5:
#     print("Ure underweight, eat some Mc\'donalds idiot")
# elif bmi < 25:
#     print("Ure good, keep going like that motherfucker!")
# elif bmi < 30:
#     print("GO and walk a bit, u\'re overweight.")
# elif bmi < 35:
#     print("Hohooo, u\'re ugly animal, stop eating cause u\'re obese")
# else:
#     print("That's clinical bro, order a train to keep u to a doctor meatball.")

# yr = int(input("The leap year calculator, type the year you want here: "))
#
# if yr % 2 == 0:
#     if yr % 4 == 0 and yr % 100 != 0 and yr % 400 != 0:
#         print("That year is Leap.")
#     else:
#         print("That year is not leap, try more bitch!.")
# else:
#     print("That year is odd, you no brain idiot - why are you writing it?.")

# a = int(input("scrie 10 blea"))
# if not a <4 and a == 10:
#     print("nu da blea, huli teai gandit dalbanule")
# if a != 10:
#     print("10 ebanat si esti, greu de gandit cu IQ din 2 numere ?")

# print("WelCUM tu the Love score")
# name1 = input("Type your full name here:\n")
# name2 = input("Type the full name of your potential partner:\n")
#
# name1_low = name1.lower()
# name2_low = name2.lower()
# names_low = name1_low + name2_low
#
# count_T = int(names_low.count("t"))
# count_r = int(names_low.count("r"))
# count_u = int(names_low.count("u"))
# count_e = int(names_low.count("e"))
# total1 = str(count_T + count_r + count_u + count_e)
#
# count_L = int(names_low.count("l"))
# count_o = int(names_low.count("o"))
# count_v = int(names_low.count("v"))
# count_e = int(names_low.count("e"))
# total2 = str(count_L + count_o + count_v + count_e)
#
# total = int(total1 + total2)
#
# if total < 10 or total > 90:
#     print(f"Your score is {total}, you go together like Coke and Mentos.")
# elif total > 40 or total < 50:
#     print(f"Your score is {total}, you\'re good together.")
# else:
#     print(f"Your score is {total}")

import sys


def you_died(reason):
    print(f"You died [Sad music ♩ ♪ ♫ ♬].\n{reason}")
    sys.exit()


print("Welcome to the \"Dark letters\", a souls like text game which will test your patience, [Evil laugh]")

left = "left"
right = "right"
answer = input("Good, let's start the game. "
               "You woke up in the middle of an emtpy road, you have choice to walk forward,\n"
               f"and turn [{left}] or [{right}], which direction will you choose? ")
if answer.lower() != left:
    you_died("You had been hit by a car.")

sportsCar = "BMW"
bus = "bus"
answer = input(f"You see in front of you very nice [{sportsCar}] and an old [{bus}] and you decided to drive one,\n"
               "which one will you choose? ")
if answer.lower() != bus:
    you_died("During oversteer when you tried to start with Launch-control,\n"
             "you drove directly in a pillar next to you, your car stared burning with you inside.")

hotdog = "hotdog"
burger = "burger"
answer = input("You decided to stop and buy something to eat, because you feel hungry.\n"
               f"You found a Take away place, you have a choice between a [{burger}] or a [{hotdog}]? ")
if answer.lower() != burger:
    you_died(f"You made a bite of your tasty {hotdog}, when suddenly came the famous Samurai,\n"
             "named \"Burger Lover\". He saw you eating and extremely fast took his Katana named \"HotDog Slicer\",\n"
             "and sliced your arm and your head from your neck. When your head was falling,\n"
             "you saw his laughing face saying, \"Die dirty hotdog eater\".")

print("That was a right choice, you started to eat your burger like an animal, from the side it was looking,\n"
      "like you were making love, when suddenly from neither next to you appeared one famous Samurai,\n"
      "named \"Burger Lover\". He saw you tasting this burger, and asked you how long do you love burgers.\n"
      "You were talking the whole evening and spent time really good communicating together. That was a good day.")
