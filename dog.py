kgprice = 5.5
probablekg = int(input("How many kilos do you think is going to be enough: "))
total_food = 0
while True:
    daily_grams = int(input("How many grams did the dog eat today: "))
    total_food = total_food + daily_grams
    if daily_grams == 0:
        break
money_spent = kgprice * (total_food/1000)
money_spent = round(money_spent, 2)
if probablekg*1000 >= total_food:
    print(f"The food is enough! Leftovers {probablekg*1000 - total_food} grams.")
    print(f"You spent {money_spent} leva for the food!")
else:
    print(f"The food isn't enough! You need {total_food - probablekg*1000} grams more.")
    print(f"You spent {money_spent} leva for the food!")