# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
my_cart = {}


def addToCart():
    item = input("What do you want to add?")
    quantity = input("How many items do you want? (Please input a number)")
    my_cart[item] = quantity


def showCart():
    print(my_cart)


def removeFromCart():
    item = input("Which item do you want to remove from your cart?")
    if item in my_cart:
        # remove item here
        del my_cart[item]
        print(f"Successfully removed {item} from your cart")
    else:
        print("You don't have that item in your cart")


def run():
    while True:
        answer = input("What do you want to do? (show/add/delete/quit)")
        if answer.lower() == "quit":
            showCart()
            break
        elif answer.lower() == "add":
            # do add function here
            addToCart()
        elif answer.lower() == "show":
            showCart()
        elif answer.lower() == "delete":
            removeFromCart()
        else:
            print("Invalid response")


run()
