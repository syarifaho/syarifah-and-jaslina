import random

def main():
    """Start an element guessing game."""
    print("Guess a random element!")

    element =[
        "magnesium",
        "boron",
        "lithium",
        "hydrogen",
        "carbon",
        "sodium",
        "nitrogen",
        "oxygen",
        "beryllium",
        "neon",
        "helium",
        "fluorine",
        ]
    """untuk menghasilkan jawapan random yang perlu diteka"""
    x = random.choice(element)
    print(x)
    guess = None
    """diberikan hint untuk pemain meneka"""
    while x != guess:

        guess = str(input("what element am i thinking of"))

        if x == guess:
            print("You guessed {}.Congralutations you guessed it right!".format(guess))
        elif x == "magnesium":
            print("HINT:completely filled outer s orbital")
        elif x ==("boron"):
            print("HINT:poor conductor of electricity")
        elif x == "lithium":
            print("HINT:soft and silvery white")
        elif x == "hydrogen":
            print("HINT:colorless gas")
        elif x == "carbon":
            print("HINT:soft,dull and grey in colour")
        elif x == "sodium":
            print("HINT:strong metallic lustre")
        elif x == "nitrogen":
            print("HINT:colorless,odorless and tasteless")
        elif x == "oxygen":
            print("HINT:tasteless gas")
        elif x == "beryllium":
            print("HINT:steel-gray,strong")
        elif x == "neon":
            print("HINT:inert monatomic")
        elif x == "hellium":
            print("HINT:low boiling point")
        elif x == "fluorine":
            print("HINT:univalent poisonous gaseous halogen")

main()

