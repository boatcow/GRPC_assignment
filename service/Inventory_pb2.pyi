from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AVAILABLE: Status
DESCRIPTOR: _descriptor.FileDescriptor
FICTION: Genre
MYSTERY: Genre
NON_FICTION: Genre
SCIFI: Genre
TAKEN: Status

class Book(_message.Message):
    __slots__ = ["Author", "Genre", "ISBN", "PublishingYear", "Title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    Author: str
    GENRE_FIELD_NUMBER: _ClassVar[int]
    Genre: str
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    PublishingYear: int
    TITLE_FIELD_NUMBER: _ClassVar[int]
    Title: str
    def __init__(self, ISBN: _Optional[str] = ..., Title: _Optional[str] = ..., Author: _Optional[str] = ..., Genre: _Optional[str] = ..., PublishingYear: _Optional[int] = ...) -> None: ...

class BookCreateRequest(_message.Message):
    __slots__ = ["Author", "Genre", "ISBN", "PublishingYear", "Title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    Author: str
    GENRE_FIELD_NUMBER: _ClassVar[int]
    Genre: Genre
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    PublishingYear: int
    TITLE_FIELD_NUMBER: _ClassVar[int]
    Title: str
    def __init__(self, ISBN: _Optional[str] = ..., Title: _Optional[str] = ..., Author: _Optional[str] = ..., Genre: _Optional[_Union[Genre, str]] = ..., PublishingYear: _Optional[int] = ...) -> None: ...

class BookRetrieveRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventory_number", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: Book
    inventory_number: int
    status: Status
    def __init__(self, inventory_number: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class StandardBookResponse(_message.Message):
    __slots__ = ["Author", "Genre", "ISBN", "PublishingYear", "Title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    Author: str
    GENRE_FIELD_NUMBER: _ClassVar[int]
    Genre: str
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    PublishingYear: int
    TITLE_FIELD_NUMBER: _ClassVar[int]
    Title: str
    def __init__(self, ISBN: _Optional[str] = ..., Title: _Optional[str] = ..., Author: _Optional[str] = ..., Genre: _Optional[str] = ..., PublishingYear: _Optional[int] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: int
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
