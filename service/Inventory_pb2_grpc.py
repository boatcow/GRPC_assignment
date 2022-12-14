# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Inventory_pb2 as Inventory__pb2


class InventoryStub(object):
    """1. SERVICE
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/Inventory.Inventory/CreateBook',
                request_serializer=Inventory__pb2.BookCreateRequest.SerializeToString,
                response_deserializer=Inventory__pb2.StatusResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/Inventory.Inventory/GetBook',
                request_serializer=Inventory__pb2.BookRetrieveRequest.SerializeToString,
                response_deserializer=Inventory__pb2.StandardBookResponse.FromString,
                )


class InventoryServicer(object):
    """1. SERVICE
    """

    def CreateBook(self, request, context):
        """creates book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """fetches book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=Inventory__pb2.BookCreateRequest.FromString,
                    response_serializer=Inventory__pb2.StatusResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=Inventory__pb2.BookRetrieveRequest.FromString,
                    response_serializer=Inventory__pb2.StandardBookResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Inventory.Inventory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inventory(object):
    """1. SERVICE
    """

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inventory.Inventory/CreateBook',
            Inventory__pb2.BookCreateRequest.SerializeToString,
            Inventory__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inventory.Inventory/GetBook',
            Inventory__pb2.BookRetrieveRequest.SerializeToString,
            Inventory__pb2.StandardBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
