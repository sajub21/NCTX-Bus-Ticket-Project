from classes import Admin

def display_customer_menu():
    """Customer menu"""
    userR = True
    while userR:
        print("\n==== Customer Display ====")
        print("1. View available ticket categories")
        print("2. View top-up available within category")
        print("3. View prices and details for top-ups")
        print("4. Make a Purchase")
        print("5. View purchase history")
        print("6. Exit")
        choice = input("Please enter your choice: ").strip()
        return choice
    
def display_admin_menu():
    """Admin menu"""
    userR = True
    while userR:
        print("\n=== Admin Panel ===")
        print("1. View available ticket categories")
        print("2. View top-up types within a category")
        print("3. Update price for a top-up")
        print("4. View purchase history")
        print("5. Exit")
        choice = input("Please enter your choice: ").strip()
        return choice
    
def display_menu(current_user):
    """It Display the main menu and handle user choice"""
    if isinstance(current_user, Admin):
        return display_admin_menu()
    else:
        return display_customer_menu()
    
def browse_categories(categories):
    print("\nAvalable Categories: ")
    for cat in categories.values():
        print(f"- {cat.title} (ID: {cat.id})")

def browse_topups(category_id, categories):
    if category_id in categories:
        cat = categories[category_id]
        print(f"\nTop-ups in {cat.title}:")
        for topup in cat.topups:
            print(f"- {topup.title} (ID: {topup.id})")
    else:
        print("Category not found")
        
def view_topup_details(topup_id, categories):
    for cat in categories.values():
        for topup in cat.topups:
            if topup.id == topup_id:
                print(f"\nDetails for {topup.title}:")
                print(f"Description: {topup.description}")
                print(f"Price: £{topup.price_in_pence / 100:.2f}")
                print(f"Entitlement: {topup.entitlement_type}, {topup.entitlement_unit} {topup.entitlement_value}")
                print(f"Quantity: {topup.entitlement_quantity}")
    print("Top-up not found")
    
def view_purchase_history(purchases):
    if not purchases:
        print("No purchases yet")
        return
    print("\nPurchase histoty:")
    for p in purchases:
        print(f"- Top-up ID: {p.topup_id}, Quantity: {p.quantity}, Total: £{p.total_price / 100:.2f }, Time: {p.timestamp}")
        
# It write ticket receipt to customer
def write_receipt(purchase, topup):
    """Write a receipt file for the puchase"""
    filename = f"receipt_{purchase.timestamp.replace(':', '-').replace('.', '-')}.txt"
    try:
        with open(filename, 'w') as file:
            file.write("=== NCTX Bus Ticket Receipt ===\n")
            file.write(f"Timestamp: {purchase.timestamp}\n")
            file.write(f"Top-up: {topup.title}\n")
            file.write(f"Description: {topup.description}\n")
            file.write(f"Quantity: {purchase.quantity}\n")
            file.write(f"Unit Price: £ {topup.price_in_pence / 100:.2f}\n")
            file.write(f"Total price: £ {purchase.total_price / 100:.2f}\n")
            file.write(f"Entitlement: {topup.entitlement_type}, {topup.entitlement_value} {topup.entitlement_unit}\n")
            file.write(f"Thank you for your purchase\n")
        print(f"Receipt saved to {filename}")
    except Exception as e:
        print(f"error writing receipt: {e}")