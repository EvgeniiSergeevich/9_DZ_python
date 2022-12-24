import model

def run_game():
    candies = model.candies
    while candies > 0:
        print(model.user_logic(input('Сколько конфет забираете? ')))
        print(model.won())
        if model.candies == 0:
            exit()
        print(model.bot_logic())
        print(model.won())
        if model.candies == 0:
            exit()

run_game()