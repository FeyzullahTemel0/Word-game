
# Kelime Tahmin Oyunu
import random


def pick_random_word():
    word_list = ["python", "c", "java", "swift", "html", "css", "go", "ruby"]
    random_word = random.choice(word_list)
    return random_word


def make_word_classified(word):
    classified_list = ["_" for i in word]
    return classified_list


def guess():
    word = pick_random_word()
    classified_word = make_word_classified(word)
    print(*classified_word)
    total_attempts = 0

    while True:
        try:
            answer = input("Guess a letter (Write only one letter)>: ").upper()
            if len(answer) > 1:
                raise Exception
        except Exception:
            print("Only one letter at a time!")
            continue
        total_attempts += 1

        if total_attempts >= 7:
            print("Sorry but you lost!")
            try_again = input("Wanna play again? (write y or n) >: ")
            if try_again == 'y':
                guess()
            elif try_again == 'n':
                print("Goodbye!")
                quit()

        for i in range(len(word)):
                if answer == word[i]:
                    classified_word[i] = answer
                if "".join(classified_word) == word:
                    print("You won!")
                    quit()

        print(*classified_word, f"\nTotal attempts left: {7 - total_attempts}")


guess()