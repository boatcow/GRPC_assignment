import uuid
class Inventory:

    def __init__(self):
        self.inventory=[]
    def add_book(self,book):
        inv={
        "inventory_number":str(uuid.uuid4()),
        "book" : book
        }
        self.inventory.append(inv)
    def get_book(self,isbn):
        for current_book in self.inventory:
            if current_book["book"].get("ISBN",None) == isbn:
                return(current_book["book"])
