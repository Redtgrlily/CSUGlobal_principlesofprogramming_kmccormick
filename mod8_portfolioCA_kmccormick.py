class ItemToPurchase: 
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="June 3, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_item(self, item):
        self.cart_items.append(item)
        
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
            if not found:
                print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")
        
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()
    
    def print_menu(cart):
        menu = (
            "\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n"
        )
        while True:
            print(menu)
            choice = input("Choose an option:\n").lower()
            
            if choice == 'a':
                print("Add item to cart")
                name = input("Enter the item name:\n")
                description = input("Enter the item description:\n")
                price = float(input("Enter the item price:\n"))
                quantity = int(input("Enter the item quantity:\n"))
                item = ItemToPurchase(name, price, quantity, description)
                cart.add_item(item)
            
            elif choice == 'r':
                print("Remove item from cart")
                name = input("Enter the name of item to remove:\n")
                cart.remove_item(name)
                
            elif choice == 'c':
                print("Change item quantity")
                name = input("Enter the item name:\n")
                quantity = int(input("Enter the new quantity:\n"))
                modified_item = ItemToPurchase(name=name, quantity=quantity)
                cart.modify_item(modified_item)
                
            elif choice == 'i':
                print("Output items' descriptions")
                cart.print_descriptions()
                
            elif choice == 'o':
                print("Output shopping cart")
                cart.print_total()
                
            elif choice == 'q':
                break
            
            else:
                print("Invalid option. Please try again.")
                
def main():
        customer_name = input("Enter customer's name:\n")
        current_date = input("Enter today's date:\n")
        print(f"\nCustomer name: {customer_name}")
        print(f"Today's date: {current_date}")
        
        cart = ShoppingCart(customer_name, current_date)
        ShoppingCart.print_menu(cart)
        
if __name__ == "__main__":
        main()