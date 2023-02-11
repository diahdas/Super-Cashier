from transaction import Transaction
from tabulate import tabulate

def main_menu():
    """User interface layout"""

    # main menu interface
    print("Welcome to ANDI SUPERMARKET!")
    print("1. Create New Transaction")
    print("2. Exit")

    while True:
        print("----------------------------")
        choice = input("Enter task no: ")
        print("----------------------------")

        if choice == "1":
            # menu after user choose create new transaction
            print("1. Add Item")
            print("2. Update Item Name")
            print("3. Update Item Quantity")
            print("4. Update Item Price")
            print("5. Delete Item")
            print("6. Reset Transaction")
            print("7. Check Order")
            print("8. Total Price")
            print("9. Exit")

            # create transaction object
            new_transaction = Transaction()

            # move to transaction menu
            transaction_menu(new_transaction)

            break   
        elif choice == "2":
            exit()
            break
        else: 
            print("Input is incorrect.")

def transaction_menu(new_transaction):
    """User interface when user choose to create new transaction"""

    while True:
        print("----------------------------")
        choice = input("Enter action no: ")

        if choice == "1":
            print("Add Item")
            print("----------------------------")

            nama_item = input("Input item's name: ")

            while True:
                try:
                    jumlah_item = int(input("Input item's quantity: "))
                    break
                except ValueError:
                    print("Please input integer value.")
                    continue

            while True:
                try:
                    harga_item = int(input("Input item's price: "))
                    break
                except ValueError:
                    print("Please input integer value.")
                    continue

            print("----------------------------")
            new_transaction.add_item(nama_item, jumlah_item, harga_item)
            print("Item added successfully.")
            print(tabulate(new_transaction.df_item, headers="keys", tablefmt="grid"))

            transaction_menu(new_transaction)
            break
        elif choice == "2":
            print("Update Item Name")
            print("----------------------------")

            nama_item = input("Input item's name: ")
            update_nama_item = input("Update item's name: ")

            print("----------------------------")
            new_transaction.update_item_name(nama_item, update_nama_item)
            print("Item's name changed")
            print(tabulate(new_transaction.df_item, headers="keys",tablefmt="grid"))

            transaction_menu(new_transaction)
            break
        elif choice == "3":
            print("Update Item Quantity")
            print("----------------------------")

            nama_item = input("Input nama item: ")

            while True:
                try:
                    update_jumlah_item = int(input("Update item's quantity: "))
                    break
                except ValueError:
                    print("Please input integer value.")
                    continue
            
            print("----------------------------")
            new_transaction.update_item_qty(nama_item, update_jumlah_item)
            print("Item's quantity changed")
            print(tabulate(new_transaction.df_item, headers="keys",tablefmt="grid"))

            transaction_menu(new_transaction)
            break
        elif choice == "4":
            print("Update Item Price")
            print("----------------------------")

            nama_item = input("Input nama item: ")

            while True:
                try:
                    update_harga_item = int(input("Update item's price: "))
                    break
                except ValueError:
                    print("Please input integer value.")
                    continue

            print("----------------------------")
            new_transaction.update_item_price(nama_item, update_harga_item)
            print("Item's price changed")
            print(tabulate(new_transaction.df_item, headers="keys", tablefmt="grid"))
            
            transaction_menu(new_transaction)
            break
        elif choice == "5":
            print("Delete Item")
            print("----------------------------")

            nama_item = input("Input nama item: ")

            print("----------------------------")
            new_transaction.delete_item(nama_item)
            print("Delete an item successfully")
            print(tabulate(new_transaction.df_item, headers="keys", tablefmt="grid"))

            transaction_menu(new_transaction)
            break
        elif choice == "6":
            print("Reset Transaction")
            print("----------------------------")

            new_transaction.reset_transaction()
            print("Delete all item successfully")
            print(tabulate(new_transaction.df_item, headers="keys", tablefmt="grid"))
            
            transaction_menu(new_transaction)
            break
        elif choice == "7":
            print("Check Order")
            print("----------------------------")
            
            new_transaction.check_order()
            transaction_menu(new_transaction)
            break
        elif choice == "8":
            print("Total Price")
            print("----------------------------")
            
            new_transaction.total_price()
            if new_transaction.check_order_value()==["Transaction data is correct."]:
                # menu after check total price
                print("----------------------------")
                print("1. Pay Now")
                print("2. Add another item")
                print("3. Exit")

                while True:
                    print("----------------------------")
                    choice = input("Enter action no: ")

                    if choice == "1":
                        # message
                        print("Thank you for shopping with ANDI SUPERMARKET!")

                        # ask the user whether they want to create another transaction or not
                        answer = input("Do you want to create another transaction? (yes/no): ")

                        while True:
                            if answer == "yes":
                                # back to main menu
                                main_menu()
                                break
                            elif answer == "no":
                                exit()
                                break
                            else:
                                print("Input is incorrect. Type yes/no.")
                                continue

                        break
                    elif choice == "2":
                        # back to transaction menu
                        print("1. Add Item")
                        print("2. Update Item Name")
                        print("3. Update Item Quantity")
                        print("4. Update Item Price")
                        print("5. Delete Item")
                        print("6. Reset Transaction")
                        print("7. Check Order")
                        print("8. Total Price")
                        print("9. Exit")

                        transaction_menu(new_transaction)

                        break
                    elif choice == "3":
                        exit()
                        break
                    else: 
                        print("Input is incorrect.")
                        continue
            else:
                transaction_menu(new_transaction)
            break
        elif choice == "9":
            exit()
            break
        else:
            print("Input is incorrect.")
        
def exit():
    """message if the user choose exit"""
    print("Thank you for visiting ANDI SUPERMARKET. See you next time!")

main_menu()