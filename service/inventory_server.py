from concurrent import futures
import grpc
from Inventory_pb2_grpc import InventoryServicer
from Inventory_pb2_grpc import add_InventoryServicer_to_server
import Inventory_pb2 as pb2
from Book import Book
from Inventory import Inventory
import logging

'''
We use Inventory() class to store book items

1. Internally it uses a list to keep track of the items. 
2. It assigns an unique UUID as inventory number for each unique entry to the list
3. add_book() method: creates an item if book is new else,
                    checks for duplicate entries when entering the same book twice
4. get_book() method: fetches record from the list which matches with the ID
'''
inventory=Inventory()

class InventoryServiceServicer(InventoryServicer):
    ''' 
    Server for Inventory System
    '''
    def CreateBook(self, request, context):
        print("processing request to create book inventory !")
        # create book record in inventory
        new_book=Book(request.ISBN,request.Title,request.Author,request.Genre,request.PublishingYear)
        response=inventory.add_book(new_book.get_book())
        return pb2.StatusResponse(**response)

    def GetBook(self, request, context):
        print("processing request to get book information !")
        # get book record from inventory
        response=inventory.get_book(request.ISBN)
        if response: 
            return pb2.StandardBookResponse(**response)
        return pb2.StandardBookResponse()

 
def serve():
    # setup thread pool executor workers
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # initiate server
    add_InventoryServicer_to_server(InventoryServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()