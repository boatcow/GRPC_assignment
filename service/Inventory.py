import uuid

# Keeping track of Inventories
class Inventory:

    def __init__(self):
        # Initiate inventories and load sample data
        self.inventory=[]
        base_inventories=[
        {"inventory_number": "100","book": {'ISBN': '1', 'Title': 'Test1', 'Author': 'abc', 'Genre': 'UNKNOWN', 'PublishingYear': 2010}},
        {"inventory_number": "101","book": {'ISBN': '2', 'Title': 'Test2', 'Author': 'abcd', 'Genre': 'FICTION', 'PublishingYear': 2011}}
        ]
        self.inventory+=base_inventories


    def add_book(self,book):
        
        # create a new inventory object
        inv={
        "inventory_number":str(uuid.uuid4()),
        "book" : book
        }

        # check if it already exists
        if self.get_book(book["ISBN"]):
            return {
                "message" : "Book already exists",
                "status" : 403
            }

        # add inventory record(book) to inventory
        self.inventory.append(inv)
        return {
                "message" : "Book created",
                "status":200
        }

    def get_book(self,isbn):

        # find book with matching ISBN
        for current_book in self.inventory:
            if current_book["book"].get("ISBN",None) == isbn:
                return(current_book["book"])
        return None
