print("Welcome to Python Billing System")
'''swapping the values of the variables'''
def swap(a,b):
    return b,a
'''function to calculate the total amount'''
def calculate_total_amount(items):
    total_amount = 0
    for item in items:
        total_amount += item[1]
    return total_amount