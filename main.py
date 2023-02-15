from art import logo, vs
from game_data import data
import random
from replit import clear

end_game = False
accounts_drawn = []
user_score = 0

print(logo)
print("Welcome to the Higher-Lower game...\n")
print("You must guess the highest and lowest account on Instagram in terms of followers.\n")
input("Press enter to start...")
clear()


def select_random_account():
    """Returns a random account that has never been drawn before."""
    global accounts_drawn
    
    while True:
        random_account = random.choice(data) 
        if random_account not in accounts_drawn:
            accounts_drawn.append(random_account)
            return random_account


def compare_accounts(account1, account2):
    """Compares the number of followers between 2 accounts and returns true or false depending on the user's response."""
    account1_name = account1["name"]
    account1_follower_count = account1["follower_count"]
    account1_description = account1["description"]
    account1_country = account1["country"]

    account2_name = account2["name"]
    account2_follower_count = account2["follower_count"]
    account2_description = account2["description"]
    account2_country = account2["country"]
    
    print(f"Compare A: {account1_name}, a {account1_description}, from {account1_country}.")
    print(vs)
    print(f"Against B: {account2_name}, a {account2_description}, from {account2_country}.")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_guess == "A":
        if account1_follower_count > account2_follower_count: 
            return True
        else:
            return False
    elif user_guess == "B":
        if account2_follower_count > account1_follower_count: 
            return True
        else:
            return False
    else:
        return False
        
    
while not end_game:
    print(logo)
    user_response = compare_accounts(select_random_account(), select_random_account())
    clear()
    print(logo)
    while user_response:
        user_score += 1
        print(f"You're right! Current score: {user_score}.")
        user_response = compare_accounts(accounts_drawn[-1], select_random_account())
        clear()
        print(logo)
    print(f"Sorry, that's wrong. Final score: {user_score}.")
    break
    
