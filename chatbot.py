# --- Define your function
#jokes=["What did one plate whisper to the other plate?" + time.sleep(1.5) + "Dinner is on me"]
import random
jokes = ["What did one plate whisper to the other plate?.....................DINNER IS ON ME!!! HAHAHA", "What has four wheels and flies?......................A GARBAGE TRUCK HAHAAAAHAAAA", "Why did the math book look so sad?....................BECAUSE OF ALL OF ITS PROBLEMS HAHAAAAA", "When do you have to go to the dentist? TOOTH: HURTY!!! HAHAAAAA"]

def intro():
    print("Hi! I'm chatty!")
    answer=input("What's your name?")
    print(" ")
    print("Nice to meet you" + " " + answer +"!")
    print(" ")

def actions():
    print("Would you like to hear a joke?")
    print(" ")
    print("Or maybe play rock paper scissors?")
    print(" ")
    print("Orrrrr I cAn tElL yOUr FoRtUnnee")
    print(" ")
    pick=input("Type 'j' for a joke, 'r' for rock paper scissors, 'f' for your fotune, and 'n' for nothing.")
    print(" ")
    if pick == "n":
        print("Aw :( ok. See you later then.")
    if pick == "j":
        print("Haha yes!")
        print(random.choice(jokes))
    if pick == "r":
        print("OoOOoooOOo I'm gonna beat youuuu")
        print(" ")
        attack=input("Choose rock, paper, or scissors")
        if attack=="rock":
            print("       ,--.--._")
            print("------= _, \___)")
            print("        / _/____)       8<")
            print("        \//(____)")
            print("------\     (__)")
            print("       '-----)")
            print(" ")
            print("Oh no!! You beat me! I was scissors :( ")
        if attack == "paper":
            print(" ")
            print("   _       ,/'  ________")
            print("  (_).  ,/'     |      |")
            print("  __  ::        |______|")
            print(" (__)'  `\.")
            print("            `\. ")
            print(" ")
            print("Haha! I won! I was scissors.")
        if attack == "scissors":
            print(" ")
            print("Awww we both picked scissors")
            print("   _    _")
            print("  (_)  / )")
            print("    | (_/ ")
            print("   _+/  ")
            print("   //|\ ")
            print("  // | )")
            print(" (/  |/  ")
            print(" ")
            print("I guess we tied")
    if pick == "f":
        color= input("Pick from pink, blue, black, or purple")
        if color=="pink":
            print("p, i, n, k")
            number1 = input("Pick between 7, 8, 11, and 12")
            if number1=="7":
                print("Your day will be awesome")
            if number1=="8":
                print("Later today you will find $20 on the ground")
            if number1=="11":
                print("You will see 10 dogs today(or more if you're at blizzard.)")
            if number1=="12":
                print("You are going to lick a piece of dust that was touched by Tom Cruz")
        if color=="blue":
            print("b, l, u, e")
            number1 = input("Pick between 7, 8, 11, and 12")
            if number1=="7":
                print("Your day will be awesome")
            if number1=="8":
                print("Later today you will find $20 on the ground")
            if number1=="11":
                print("You will see 10 dogs today(or more if you're at blizzard.)")
            if number1=="12":
                print("You are going to lick a piece of dust that was touched by Tom Cruz")
        if color=="black":
            print("b, l, a, c, k")
            number2= input("Pick between 3, 4, 7, and 2")
            if number2=="3":
                print("You will adopt a tiger and you will become best friends")
            if number2=="4":
                print("You will finish your project on time(unlike me)")
        if color=="purple":
            print("p, u, r, p, l, e")
            number2= input("Pick between 3, 4, 7, and 2")
            if number2=="3":
                print("You will adopt a tiger and you will become best friends")
            if number2=="4":
                print("You will finish your project on time(unlike me)")
#def main():
 # while True:
    #answer = input("(What will you say?) ")
    #print("That's cool!")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    intro()
    actions()
