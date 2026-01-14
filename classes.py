from datetime import datetime

#user class
class User:
    """basic class for users"""
    def __init__(self, username):
        self.username = username 

#admin class that ahndle and manage prices
class Admin(User):
    """Administrator user with price update capabilities"""
    def __init__(self, username):
        super().__init__(username)
        
# customer class, it them to buy ticket
class Customer(User):
    """Customer user for purchasing"""
    def __init__(self, username):
        super().__init__(username)
        
#Category class that handle category menu/hub"""
class Category:
    """Category class for bus tickets"""
    def __init__(self, category_id, title, description):
        self.id = category_id
        self.title = title
        self.description = description
        self.topups = []


    def add_topup(self, topup):
        """Add a topup to this category"""
        self.topups.append(topup)        

class TopUp:
    """topup class for with ticket option"""
    def __init__(self,
                topup_id,
                title,
                description,
                price_in_pence,
                entitlement_type,
                entitlement_unit,
                entitlement_value,
                entitlement_quantity):
        self.id = topup_id
        self.title = title
        self.description = description
        self.price_in_pence = price_in_pence
        self.entitlement_type = entitlement_type
        self.entitlement_unit = entitlement_unit
        self.entitlement_value = entitlement_value
        self.entitlement_quantity = entitlement_quantity


#handle customer purchases
class Purchase:
    def __init__(self, topup_id, quantity, timestamp=None, total_price=None):
        self.topup_id = topup_id
        self.quantity = quantity
        self.timestamp = timestamp or datetime.now().isoformat()
        self.total_price = total_price