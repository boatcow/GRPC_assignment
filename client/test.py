import unittest
from unittest.mock import Mock
import sys
from get_book_titles import get_books
from inventory_client import InventoryClient
sys.path.append('../service/')
from Inventory_pb2 import Book,StandardBookResponse


class testGetBookTitles(unittest.TestCase):

    # testing get book mock
    def test_get_book_mock(self):
        inventory_client_mock = InventoryClient()
        inventory_client_mock.get_book = Mock()
        expected = [Book(ISBN="1", Title="Test1"),
                          Book(ISBN="2", Title="Test2")]
        inventory_client_mock.get_book.side_effect = expected
        actual = get_books(inventory_client_mock, ["1", "2"])
        assert actual == expected

    # testing get book live server
    def test_get_book_live_server(self):
        inventory_client = InventoryClient()
        books = get_books(inventory_client, ["1", "2"])
        expected=[
        StandardBookResponse(Author='abc',Genre='UNKNOWN',ISBN='1',PublishingYear=2010,Title='Test1'),
        StandardBookResponse(Author='abcd',Genre='FICTION',ISBN='2',PublishingYear=2011,Title='Test2')
        ]
        assert books==expected


if __name__ == "__main__":
    unittest.main()
