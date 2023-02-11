from tabulate import tabulate
import pandas as pd

class Transaction:
    """
    A class to represent a transaction.
    
    Attributes
    ----------
    df_item : dataframe
        transaction data that consist of name, quantity, and price of the item

    Methods
    -------
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
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for transaction object.
        """

        self.df_item = pd.DataFrame({"Nama Item":[], "Jumlah Item":[], "Harga/Item":[]})

    def add_item(self, nama_item, jumlah_item, harga_item):
        '''
        Add item's name, quantity, and price to item's dataframe

        Parameters
        ----------
        nama_item : str 
            item's name
        jumlah_item : int 
            item's quantity
        harga_item : int 
            item's price

        Returns
        -------
        None 
        '''
        added_item = [nama_item, jumlah_item, harga_item]
        column_name =["Nama Item", "Jumlah Item", "Harga/Item"]
        self.df_item.loc[len(self.df_item.index),column_name] = added_item

    def update_item_name(self, nama_item, update_nama_item):
        '''
        Update specific item's name

        Parameters
        ----------
        nama_item : str 
            item's name
        update_nama_item : str 
            updated item's name
            
        Returns
        -------
        None 
        '''
        match_item = self.df_item["Nama Item"].str.fullmatch(nama_item)
        self.df_item.loc[match_item, "Nama Item"] = update_nama_item
    
    def update_item_qty(self, nama_item, update_jumlah_item):
        '''
        Update item's quantity based on specific item's name

        Parameters
        ----------
        nama_item : str 
            item's name
        update_jumlah_item : int
            updated item's quantity
            
        Returns
        -------
        None 
        '''
        match_item = self.df_item["Nama Item"].str.fullmatch(nama_item)
        self.df_item.loc[match_item, "Jumlah Item"] = update_jumlah_item
    
    def update_item_price(self, nama_item, update_harga_item):
        '''
        Update item's price based on specific item's name

        Parameters
        ----------
        nama_item : str 
            item's name
        update_jumlah_item : int
            updated item's price
            
        Returns
        -------
        None 
        '''
        match_item = self.df_item["Nama Item"].str.fullmatch(nama_item)
        self.df_item.loc[match_item, "Harga/Item"] = update_harga_item
    
    def delete_item(self, nama_item):
        '''
        Delete item based on specific item's name

        Parameters
        ----------
        nama_item : str 
            item's name
            
        Returns
        -------
        None 
        '''
        match_item = self.df_item["Nama Item"].str.fullmatch(nama_item)
        self.df_item = self.df_item[~match_item].reset_index(drop=True)
    
    def reset_transaction(self):
        '''
        Delete all item

        Parameters
        ----------
        None
            
        Returns
        -------
        None 
        '''
        self.df_item=self.df_item.head(0)
    
    def check_order_value(self):
        '''
        Check whether the value of items that have been inputed is correct or not
        '''

        output = []


        if self.df_item.empty:
            output.append("No items added")
        else:
            if "" in self.df_item["Nama Item"].str.strip().values:
                output.append("Item's name can't be blank.")
            if 0 in self.df_item["Jumlah Item"].values:
                output.append("Item's quantity can't be 0.")
            if 0 in self.df_item["Harga/Item"].values:
                output.append("Item's price can't be 0.")

        if output == []:
            output = ["Transaction data is correct."]

        return output

    def check_order(self):
        '''
        Check whether the value of items that have been inputed is correct or not
        and show the transaction data
        '''

        output = self.check_order_value()
        
        if output==["Transaction data is correct."]:
            self.df_item["Total Harga"]= self.df_item["Jumlah Item"] * self.df_item["Harga/Item"]
        
        print("\n".join(output))
        print(tabulate(self.df_item, headers="keys", tablefmt="grid"))
    
    def total_price(self):
        '''
        Calculate subtotal, discount, and total amount to be paid
        '''
        if self.check_order_value() == ["Transaction data is correct."]:
            self.df_item["Total Harga"]= self.df_item["Jumlah Item"] * self.df_item["Harga/Item"]
            subtotal = self.df_item["Total Harga"].sum()

            discount = 0
            if subtotal > 500_000:
                discount = 0.1
            elif subtotal > 300_000:
                discount = 0.08
            elif subtotal > 200_000:
                discount = 0.05
            else: 
                discount = 0

            total = subtotal * (1 - discount)

            print(tabulate(self.df_item, headers="keys", tablefmt="grid"))
            print(f"Subtotal = Rp{subtotal: ,.0f}\nDiscount = {discount: .0%}\nTotal = Rp{total: ,.0f}")
            print("----------------------------")
            print(f"The total amount to be paid is Rp{total: ,.0f}")
        else:
            print("\n".join(self.check_order_value()))
