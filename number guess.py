import random
try:
    max_num = int(input("give a max num: "))
    def roll_dice(num):
        return random.randint(1, num)
    number = roll_dice(max_num)
    guess = ""
    tries = 10
    try_count = 0
    out_of_tries = False
    while guess != number and not(out_of_tries):
        guess = int(input("Guess a number: "))
        if guess > max_num:
            print("Can't guess above " + str(max_num))
            try_count += 1
        else:
            if guess < number:
                print(">")
                try_count += 1
            elif guess > number:
                print("<")
                try_count += 1
            else:
                print("CORRECT")
        if try_count == tries:
            out_of_tries = True
    if out_of_tries:
        print("Out Of Tries")
except ValueError:
    print("Value Input Error")
except:
    print("ERROR")

