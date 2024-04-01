# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent

def solve(meal_cost_, tip_percent_, tax_percent_):
    tip = (meal_cost_/100)*tip_percent_
    tax = (tax_percent_/100)*meal_cost_
    total = meal_cost_ + tip + tax
    print(total)


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
