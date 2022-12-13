import Inventory_pb2_grpc as pb2_grpc
import Inventory_pb2 as pb2
import grpc

class InventoryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        self.stub = pb2_grpc.InventoryStub(self.channel)

    def add_book(self):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.BookCreateRequest(ISBN="1",Title="Hello Server you there?",Author="abc",Genre="efd",PublishingYear=2130)
        return self.stub.CreateBook(message)


    def get_book(self):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.BookRetrieveRequest(ISBN="1")
        print(f'{message}')
        return self.stub.GetBook(message)

if __name__ == '__main__':

    client = InventoryClient()
    print("adding book")
    result = client.add_book()
    print(f'{result}')
    print("fetching book")
    result = client.get_book()
    print(f'{result}')
    while(1):
        pass


    # string Title =1;
    # string Author =2;
    # string Genre =3;
    # int32 PublishingYear =4;
