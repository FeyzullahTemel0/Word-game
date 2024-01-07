import random

def load_word_list():
    with open("word_list.txt", "r") as file:
        word_list = file.read().splitlines()
    return word_list

def pick_random_word():
    word_list = load_word_list()
    random_word = random.choice(word_list)
    return random_word.upper()

def make_word_classified(word):
    classified_list = ["_" if letter.isalpha() else letter for letter in word]
    return classified_list

def guess():
    word = pick_random_word()
    classified_word = make_word_classified(word)
    print(" ".join(classified_word))
    total_attempts = 0
    max_attempts = int(input("Enter the number of attempts you want to have: "))

    while total_attempts < max_attempts:
        try:
            answer = input("Guess a letter (Write only one letter): ").upper()
            if len(answer) != 1 or not answer.isalpha():
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a single letter.")
            continue

        total_attempts += 1

        if answer in word:
            for i in range(len(word)):
                if answer == word[i]:
                    classified_word[i] = answer
            print(" ".join(classified_word))
            if "".join(classified_word) == word:
                print("Congratulations! You won!")
                break
        else:
            print("Incorrect guess. Try again.")
        
        print(f"Total attempts left: {max_attempts - total_attempts}")

    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    guess()
