# Super-Cashier

### Background
A big supermarket in a city in Indonesia want to improve their business process. They want to create a self-service cashier so the customers can add item's name, quantiy, and price by themself. By this cashier system, they also hope that people who are out of town can buy goods from their supermarket.

### Requirement
- Create ID transaction using class object
- Add item's name, quantity, and price
- Update item's name, quantity, and price
- Delete item
- Reset transaction (delete all item)
- Check whether item's name, quantity, and price is correct or not
- Check total price after discount

### Flowchart
<img src="img/flowchart.png" width="500"/>

From the main menu, customer can create new transaction to start add item or exit to close the program. From transaction, customer can add item, update item's name, update item's quantity, update item's price, delete an item, delete all item, check whether the inputed value is correct or not, and check total price. After the customer check the total price, there will be options to pay the transaction now, add another item, or exit if they want to cancel the order. In the end after they choose pay now, user will be asked whether they want to create another transaction or not.   

### Functions
add_item(nama_item, jumlah_item, harga_item):
    Add item's name, quantity, and price to item's dataframe.
update_item_name(nama_item, update_nama_item):
    Update specific item's name
update_item_qty(nama_item, update_jumlah_item):
    Update item's quantity based on specific item's name
update_item_price(nama_item, update_harga_item):
    Update item's price based on specific item's name
delete_item(nama_item):
    Delete item based on specific item's name
reset_transaction():
    Delete all item
check_order_value():
    Check whether the value of items that have been inputed is correct or not
check_order():
    Check whether the value of items that have been inputed is correct or not
    and show the transaction data
total_price():
    Calculate subtotal, discount, and total amount to be paid

### Test Case
- Test Case 1 : Add Item

    <img src="img/test%20case%201.PNG" width="500"/>
- Test Case 2 : Delete Item

    <img src="img/test%20case%202.PNG" width="500"/>
- Test Case 3 : Reset Transaction

    <img src="img/test%20case%203.PNG" width="500"/>
- Test Case 4 : Check Total Price

    <img src="img/test%20case%204.PNG" width="500"/>
