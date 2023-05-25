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

    customer['bag'] = []

    print("\n*************************")

    print(f"Hello, {customer['name']}!\nGlad to see U in 'xeShop'")

    print("*************************\n")

    print("Choose something for your boyfriend:\n")

    while customer['balance'] >= 0:
        i = 1

        for goods, price in store.items():
            print(f"{i}) {goods.upper()} - {price} $")

            i += 1
        print("q) QUIT")

        user_choose = input("What do you want?\n").lower()

        # if user_choose in store:

        for choosen_goods in store.keys():

            if choosen_goods == user_choose:

                customer["balance"] -= store[choosen_goods]

                customer['bag'].append({choosen_goods: store[choosen_goods]})

                print(f"\n{choosen_goods.upper()} by {store[choosen_goods]}$ added in your bag")

                print(f"\nYour Bag:\n{customer['bag']}\n")

                print(f"You have {customer['balance']}$. Do you need something else?")

            elif user_choose == "q":

                print(f"Your boyfriend will be sad((( Goodbye, {customer['name']}")

                return False

        del store[user_choose]

if __name__ == "__main__":
    main()
