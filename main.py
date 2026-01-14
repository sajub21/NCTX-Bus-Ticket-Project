from classes import Admin, Purchase
from data_handler import load_data, load_purchases, save_purchases
from login import login
from design import display_menu, browse_categories, browse_topups, view_topup_details, view_purchase_history, write_receipt

class BusTicketSystem:
    """Manin system class it manage bus ticket data and purchases."""
    def __init__(self, csv_file='mobile_products.csv', purchase_file='purchase.csv'):
        self.csv_file = csv_file
        self.purchase_file = purchase_file
        self.categories = load_data(csv_file)
        self.purchases = load_purchases(purchase_file)
        self.current_user = None 
        
    def run(self):
        """Run the system"""
        self.current_user = login()
        self.main_loop()
        
    def main_loop(self):
        """Main Menu Loop"""
        userResponse = True
        while userResponse:
            choice = display_menu(self.current_user)
            if choice == '1':
                browse_categories(self.categories)
            elif choice == '2':
                cat_id = input("please enter category ID:  ").strip()
                browse_topups(cat_id, self.categories)
            elif choice == '3':
                if isinstance(self.current_user, Admin):
                    topup_id = input("Please enter top-up ID to update: ").strip()
                    self.update_price(topup_id)
                else:
                    view_topup_details(None, self.categories)
            elif choice == '4':
                if isinstance(self.current_user, Admin):
                    view_purchase_history(self.purchases)
                else:
                    self.make_purchase()
            elif choice == '5':
                if isinstance(self.current_user, Admin):
                    save_purchases(self.purchase_file, self.purchases)
                    print("Existing.. Purchases saved")
                    userResponse = False
                else:
                    view_purchase_history(self.purchases)
            elif choice == '6':
                save_purchases(self.purchase_file, self.purchases)
                print("Existing.. Purchases saved")
                userResponse = False
            else:
                print("Invalid choice. Please try again")
                
    def make_purchase(self, topup_id=None, quantity=None):
        if topup_id is None:
            print("To find top-up ID, use option 2 to find categories and top-up.")
            topup_id = input("Please enter top-up ID to purchase: ").strip()
        if quantity is None:
            quantity_str = input("Please enter quantity: ").strip()
            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid quantity")
                return 
            
        for cat in self.categories.values():
            for topup in cat.topups:
                if topup.id == topup_id:
                    total_price = topup.price_in_pence * quantity
                    
                    purchase = Purchase(topup_id, quantity, total_price=total_price)
                    self.purchases.append(purchase)
                    print(f"Purchase successful! Total: £{total_price / 100:.2f}")
                    #write receipt for customer
                    write_receipt(purchase, topup)
                    return
        print("Top-up not found")
    # Admin can update price and manage system
    def update_price(self, topup_id):
        """Update price for a top-up (admin only)"""
        for cat in self.categories.values():
            for topup in cat.topups:
                if topup.id == topup_id:
                    new_price_str = input(f"Current price: £{topup.price_in_pence / 100:.2f}. Enter new price in pence: ").strip()
                    try:
                        new_price = int(new_price_str)
                        if new_price < 0:
                            raise ValueError
                        topup.price_in_pence = new_price
                        print("Price updated successfully")
                        return
                    except ValueError:
                        print("Invalid price")
                        return
        print("Top-up not found")
        
if __name__ == "__main__":
    system = BusTicketSystem()
    system.run()
