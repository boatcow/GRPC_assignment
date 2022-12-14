import sys
sys.path.append('../service/')
import Inventory_pb2_grpc as pb2_grpc
import Inventory_pb2 as pb2
import grpc
import logging
class InventoryClient(object):
    """
    Client for Inventory System
    """

    def __init__(self,host='localhost',server_port=50051):
        # set host and port , defaultly resorts to localhost
        self.host = host
        self.server_port = server_port

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        self.stub = pb2_grpc.InventoryStub(self.channel)

    def add_book(self,ISBN,Title,Author,Genre,PublishingYear):
        """
        Client function to call the rpc for Adding Book to Inventory DB 
        """
        message = pb2.BookCreateRequest(ISBN=ISBN,Title=Title,Author=Author,Genre=Genre,PublishingYear=PublishingYear)
        return self.stub.CreateBook(message)


    def get_book(self,ISBN):
        """
        Client function to call the rpc for Getting Book from Server
        """
        message = pb2.BookRetrieveRequest(ISBN=ISBN)
        return self.stub.GetBook(message)

if __name__ == '__main__':
    
    # initiate client
    client = InventoryClient()

    # setup logging configs
    logging.basicConfig()

    # Sample testing requests
    print("\n---------ADDING BOOK SAMPLE TEST---------\n")
    result = client.add_book(ISBN="1000",Title="Harry Potter",Author="abc",Genre="MYSTERY",PublishingYear=1998)
    print(f'result: {result}')
    print("\n---------FETCHING BOOK SAMPLE TEST---------\n")
    result = client.get_book(ISBN="2")
    print(f'result: {result}')

