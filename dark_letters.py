

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
