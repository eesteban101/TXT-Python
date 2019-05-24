"""
    Eduardo Esteban, TXT Fellow

    This is the file that asks the user for a name, and prints it out
    back to them. Asks for an order, and repeats until order is correct.
    Terminates after order is finished.
"""
from pip._vendor.distlib.compat import raw_input


# Returns true if the order was correct, false otherwise. Makes sure for valid input
def order_is_correct(order_name):
    correct = raw_input("Is '" + order_name + "' the order you wanted? [Y] or [N]")

    while correct.lower() != 'y' and correct.lower() != 'n':
        correct = raw_input("Invalid input. Please type either 'Y' or 'N'")

    if correct.lower() == 'y':
        return True
    else:
        return False


# Returns true if user wants another order, false if not, or asks again
# for a valid input
def another_order():
    order_again = raw_input("Would you like another order? [Y] or [N] ")

    if order_again.lower() == 'y':
        return True
    elif order_again.lower() == 'n':
        print()
        return False
    else:
        print("Invalid input. Please type either 'Y' or 'N' ")
        return another_order()


# Main function, in charge of adding to the array with orders the user wants
# and repeats until they want no more.
def order(orders_arr):

    # fence-post problem: must ask at least once before you can ask again
    order_name = raw_input("What would you like? ")
    while not order_is_correct(order_name):
        order_name = raw_input("So sorry, what is your order then? ")
    print("Great! You ordered: " + order_name)
    orders_arr.append(order_name)

    # Continues to ask for input if the user has more orders
    while another_order():
        order_name = raw_input("What would you like? ")
        while not order_is_correct(order_name):
            order_name = raw_input("So sorry, what is your order then? ")
        print("Great! You ordered: " + order_name)
        orders_arr.append(order_name)


# Main function, in charge of asking user for input and prints orders
# to the console
def main():
    orders_arr = []

    print("Welcome to Food-Order!")
    print()
    name = raw_input("What is your name? ")
    print("Alright! Your name is: " + name + " Welcome!")
    order(orders_arr)
    print(name + " ordered the following:")

    # Prints the elements in the array
    for x in orders_arr:
        print(x)


if __name__ == "__main__":  # boilerplate
    main()
