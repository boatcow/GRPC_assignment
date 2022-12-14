from inventory_client import InventoryClient


def get_books(client, isbn_list):
    book_list = []
    for isbn in isbn_list:
        book = client.get_book(isbn)
        book_list.append(book)
    return book_list


if __name__ == "__main__":
    get_books(InventoryClient(), ["1", "2"])
