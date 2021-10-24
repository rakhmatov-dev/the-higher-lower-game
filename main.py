from random import choice
from art import logo, vs
from game_data import data


def print_dictionary(beginning_str, dictionary):
    print(
        beginning_str + f" {dictionary['name']}, a {dictionary['description'].lower()}, from {dictionary['country']}.")


def compare(dictionary_A, dictionary_B):
    if dictionary_A['follower_count'] > dictionary_B['follower_count']:
        return 'A'
    else:
        return 'B'


points = 0
while True:

    print(logo)
    if points == 0:
        dictionary_A = choice(data)
    print_dictionary("Compare A:", dictionary_A)

    print(vs)
    dictionary_B = choice(data)
    print_dictionary("Against B:", dictionary_B)
    if input("Who has more followers? Type 'A' or 'B': ") == compare(dictionary_A, dictionary_B):
        points += 1
        print(f"You're right! Current score: {points}.")
        dictionary_A = dictionary_B
    else:
        print(f"Sorry, that's wrong. Final score: {points}.")
        break