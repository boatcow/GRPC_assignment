import sys

sys.path.append('../service/')
import Inventory_pb2_grpc as pb2_grpc
import Inventory_pb2 as pb2
import grpc

class InventoryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self,host='localhost',server_port=50051):
        self.host = host
        self.server_port = server_port

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        self.stub = pb2_grpc.InventoryStub(self.channel)

    def add_book(self,ISBN,Title,Author,Genre,PublishingYear):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.BookCreateRequest(ISBN=ISBN,Title=Title,Author=Author,Genre=Genre,PublishingYear=PublishingYear)
        return self.stub.CreateBook(message)


    def get_book(self,ISBN):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.BookRetrieveRequest(ISBN=ISBN)
        print(f'{message}')
        return self.stub.GetBook(message)

if __name__ == '__main__':

    client = InventoryClient()

    
    print("\n---------TESTING ADDING BOOK----------------\n")
    result = client.add_book(ISBN="1000",Title="Harry Potter",Author="abc",Genre="MYSTERY",PublishingYear=1998)
    print(f'result: {result}')
    print("\n---------TESTING FETCHING BOOK----------------\n")
    result = client.get_book(ISBN="2")
    print(f'result: {result}')

