# bag = {}
#
#
#
# def add_goods_in_bag(store):
#
#     customer_choose = input("Choose something")
#     x = store.item[customer_choose]
#     print(x)
#
# add_goods_in_bag(store)

# def positive_balance (balance):
#     customer["Balance"] = balance
#     if balance > 0 :
#         return True
#     else:
#         print("Sorry, you have no money! AHAHA!!! Get out here!!!!")
#     return False
#
# def availability_of_goods (store):
#     if len(store) > 0 :
#         return True
#     else:
#         print("we have no goods now. See U later!")
#     return False


def hello(customer):


    customer['bag'] = []

    print("\n*************************"
          f"\nHello, {customer['name']}!\nGlad to see U in 'xeShop'\n"
          "*************************\n"
          "\nChoose something for your boyfriend:")

def print_products(store):

    i = 1

    for goods, price in store.items():

        print(f"{i}) {goods.upper()} - {price} $")

        i += 1

    print("-----------------")

def quit (user_choose, customer) :
    print("Q - Quite")

    if user_choose == "q":

        print(f"Goodbye, {customer['name']}")

        print(f"\nYour By now:\n{customer['bag']}\n")

def sell_product(user_choose, store, customer):

    if user_choose in store:

        for choosen_goods in store.keys():

            if choosen_goods == user_choose and store[choosen_goods] < customer['balance']:

                customer["balance"] -= store[choosen_goods]

                customer['bag'].append({choosen_goods: store[choosen_goods]})

                print(f"\n{choosen_goods.upper()} by {store[choosen_goods]}$ added in your bag\n"
                      
                      f"\nYour By now:\n{customer['bag']}\n"
                      
                      f"\nYou have {customer['balance']}$\n")

        del store[user_choose]


def shopping(customer, store, store_of_dogs):

    user_choose = ""

    while customer['balance'] >= 0 and user_choose != "q" and len(store) > 0:

        print_products(store)

        print_products(store_of_dogs)

        user_choose = input("What do you want?\n").lower()

        quit(user_choose, customer)

        sell_product(user_choose, store, customer)

        sell_product(user_choose, store_of_dogs, customer)

def main():
    customer = {
        "name": "Piter",
        "balance": 175
    }

    store = {
        "bilbo": 21,
        "mumbricante": 12,
        "dol": 78,
        "brator": 18,
        "suit": 55,
        "mask": 15
    }

    store_of_dogs = {
        "blonde": 150,
        "brunette": 200,
        "trance": 100,
    }

    hello(customer)

    shopping(customer, store, store_of_dogs)

if __name__ == "__main__":
    main()
