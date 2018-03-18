import random


def get_cows_and_bulls(a_list, the_guess):
    cows = 0
    bulls = 0

    for n, i in enumerate(a_list):
        if int(i) == int(the_guess[n]):
            print("whoa")
            cows += 1

    bulls = len(the_guess) - cows

    print("cows: " + str(cows))
    print("bulls: " + str(bulls))


if __name__ == "__main__":
    a = random.sample(range(0, 9), 4)

    print(a)

    guess = list(input("\nCows and Bulls! \n\nMake a guess:"))
    get_cows_and_bulls(a,guess)
