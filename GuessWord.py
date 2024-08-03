from random import shuffle
def line():
    print("=========================================")


def write_result(name, amount_of_points):
    with open("history.txt", "a") as file:
        file.write(f"\n{name} {amount_of_points}")


def calculate_played_games():
    played_games = 0
    with open("history.txt", "rt") as file:
        for word in file:
            played_games += 1
    return played_games


def max_result():
    max_point = 0
    with open("history.txt", "rt") as file:
        for word in file:
            temp_word = word.split(" ")
            point = int(temp_word[1])
            if point > max_point:
                max_point = point
    return max_point


name = input("Enter your name = ")
line()

amount_of_points = 0

with open("words.txt", "rt", encoding="utf-8") as file:
    for word in file:
        start_word = word.strip()
        letters = list(word.strip("\n"))
        shuffle(letters)
        shuffled_word = ''.join(letters)
        print(f"Guess the word : {shuffled_word}")
        answer_of_user = input("Your option = ")
        if answer_of_user == start_word:
            print(f"Correct, {start_word}!")
            amount_of_points += 40
        else:
            print(f"Incorrect! Correct answer - {start_word}")
        line()

write_result(name, amount_of_points)
print(f"Your result : {amount_of_points}")
print(f"Total played games : {calculate_played_games()}")
print(f"Max record : {max_result()}")