####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Golden Cupcake"
signature_flavors = ["signature_flavor 1", "signature_flavor 2", "signature_flavor 3"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ()
    print ()
    print ("- - - - - Our menu - - - - -")
    for k in menu:
        print ("- %s : %s KD" %(k, menu[k]))


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % (original_price))
    for n in original_flavors:
        print ("- %s" %(n))


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for n in signature_flavors:
        print ("- %s" %(n))


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    for k in menu:
        if(order == k):
            return True
    for k in original_flavors:
        if(order == k):
            return True
    for k in signature_flavors:
        if(order == k):
            return True
    return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print ("What is your order? (Enter the exact spelling of the item you want\
        . Type 'Exit' to end your order.)")
    while True:
        user_input = input()
        if(user_input == "Exit" or user_input == "exit"):
            break
        else:
          if is_valid_order(user_input):
            order_list.append(user_input)
          else:
            print ("Invalid choice ! ,try again :")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if (total >=5):
        return True
    else:
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += 2
        else:
            total += 2.750


    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for order in order_list:
        print ("- %s" %(order))
    total = get_total_price(order_list)
    print("That's be KD: %s"% (total))
    if accept_credit_card(total) == False:
        print ("This order is eligible for credit card pyement.")
    print("Thank you for shoping at %s" %(cupcake_shop_name))




