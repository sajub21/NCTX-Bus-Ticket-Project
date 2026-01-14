import csv 
import os 
from classes import Category, TopUp, Purchase

def load_data(categories_file):
    """Load categories and top-ups from csv file"""
    categories = {}
    if os.path.exists(categories_file):
        try:
            with open(categories_file, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cat_id = row['category_id']
                    if cat_id not in categories:
                        categories[cat_id] = Category(cat_id, row['category_title'], row['category_description'])
                    topup = TopUp(
                        row['topup_id'],
                        row['topup_title'],
                        row['topup_description'],
                        int(row['topup_price_in_pence']),
                        row['topup_entitlement_type'],
                        row['topup_entitlement_unit'] or None,
                        row['topup_entitlement_value'] or None,
                        int(row['topup_entitlement_quantity'] or 1)
                    )
                    categories[cat_id].add_topup(topup)
        except Exception as e:
            print(f"Error loading categories: {e}")
    return categories

def load_purchases(purchases_file):
    """Load purchase history from CSV file"""
    purchases = []
    if os.path.exists(purchases_file):
        try:
            with open(purchases_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    purchase = Purchase(
                        row['topup_id'],
                        int(row['quantity']),
                        row['timestamp'],
                        int(row['total_price']) if row['total_price'] else None
                    )
                    purchases.append(purchase)
        except Exception as e:
            print(f"Error loading purchases: {e}")
    return purchases

def save_purchases(purchases_file, purchases):
    """save purchase history to csv file"""
    try:
        with open(purchases_file, 'w') as file:
            fielnames = ['topup_id', 'quantity', 'timestamp', 'total_price']
            writer = csv.DictWriter(file, fieldnames=fielnames)
            writer.writeheader()
            for p in purchases:
                writer.writerow({
                    'topup_id': p.topup_id,
                    'quantity': p.quantity,
                    'timestamp': p.timestamp,
                    'total_price': p.total_price
                })
    except Exception as e:
        print(f"error saving purchase: {e}")