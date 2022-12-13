from concurrent import futures
import grpc
import time

from concurrent import futures # set number of workers
import grpc 

from Inventory_pb2_grpc import InventoryServicer
from Inventory_pb2_grpc import add_InventoryServicer_to_server
import Inventory_pb2 as pb2
from Book import Book
from Inventory import Inventory

inventory=Inventory()

class InventoryServiceServicer(InventoryServicer):
    # inventory=Inventory()
      
    # /creates book
    # rpc CreateBook (BookCreateRequest) returns (StandardBookResponse);
    # //fetches book
    # rpc GetBook (BookRetrieveRequest) returns (StandardBookResponse);
    def CreateBook(self, request, context):
        response={
            "ISBN" : request.ISBN,
             "Title":request.Title,
             "Author":request.Author,
             "Genre":request.Genre,
             "PublishingYear":request.PublishingYear
        }
        # ISBN,title,author,genre,publishing_year
        try:        
            new_book=Book(str(request.ISBN),str(request.Title),str(request.Author),str(request.Genre),int(request.PublishingYear))
            inventory.add_book(new_book.get_book())
        except Exception as e:
            print(e)


        return pb2.StandardBookResponse(**response)

    def GetBook(self, request, context):
        response=inventory.get_book(request.ISBN) 
        return pb2.StandardBookResponse(**response)

 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_InventoryServicer_to_server(InventoryServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()