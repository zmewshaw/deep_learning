quarter = 25
dime = 10
nickel = 5

amount_paid = 100

def get_user_input():
    cost = input("Whats the cost: ")
    return cost

def calculate_correct_amount_of_change(cost):
    change_left = amount_paid - cost
    num_quarters = change_left//quarter


def main():
    cost_of_item = get_user_input()
    calculate_correct_amount_of_change(cost_of_item)

if 1 != 2:
    print(3)