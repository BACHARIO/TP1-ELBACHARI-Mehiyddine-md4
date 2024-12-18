import random

COMBINATION_LENGTH = 4
MAX_ATTEMPTS = 10
POSSIBLE_VALUES = ['R', 'G', 'B', 'Y', 'O', 'P']  # Rouge, Vert, Bleu, Jaune, Orange, Violet

def generate_secret_combination():
    return [random.choice(POSSIBLE_VALUES) for _ in range(COMBINATION_LENGTH)]
def get_player_guess():
    while True:
        guess = input(f"Entrez une combinaison de {COMBINATION_LENGTH} couleurs parmi {POSSIBLE_VALUES} (ex: RGBY) : ").upper()
        if len(guess) != COMBINATION_LENGTH or not all(c in POSSIBLE_VALUES for c in guess):
            print("Combinaison invalide. Réessayez.")
        else:
            return list(guess)
def compare_combinations(secret, guess): 
    correct_position = sum(s == g for s, g in zip(secret, guess))
    secret_counts = {color: secret.count(color) for color in POSSIBLE_VALUES}
    guess_counts = {color: guess.count(color) for color in POSSIBLE_VALUES}
    correct_colors = sum(min(secret_counts[color], guess_counts[color]) for color in POSSIBLE_VALUES) - correct_position
    return correct_position, correct_colors
def play_game():
    print("Bienvenue au jeu Mastermind !")
    print(f"Vous devez deviner une combinaison de {COMBINATION_LENGTH} couleurs en {MAX_ATTEMPTS} essais maximum.")
    print(f"Les couleurs possibles sont : {POSSIBLE_VALUES}")
    secret_combination = generate_secret_combination()
    attempts = 0
    won = False
    while attempts < MAX_ATTEMPTS:
        print(f"\nEssai {attempts + 1}/{MAX_ATTEMPTS}")
        player_guess = get_player_guess()
        correct_position, correct_colors = compare_combinations(secret_combination, player_guess)
        print(f"Indices : {'*' * correct_position} (bien placés), {'-' * correct_colors} (mal placés)")
        if correct_position == COMBINATION_LENGTH:
            won = True
            break  
        attempts += 1
    if won:
        print("\n Félicitations ! Vous avez deviné la combinaison secrète !")
    else:
        print("\n Vous avez épuisé vos essais. La combinaison secrète était :", ''.join(secret_combination))

if __name__ == "__main__":
    play_game()
