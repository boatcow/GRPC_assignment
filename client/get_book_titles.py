from inventory_client import InventoryClient


def get_books(client, isbn_list):
    book_list = []
    for isbn in isbn_list:
        book = client.get_book(isbn)
        book_list.append(book)
    return book_list


if __name__ == "__main__":
    result=get_books(InventoryClient(host='localhost',server_port=50051), ["1", "2"])
    print("\n-------OUTPUT-------\n")
    for res in result:
        print(res)