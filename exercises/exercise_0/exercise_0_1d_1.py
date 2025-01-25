from dataclasses import dataclass

USERS = [
    {"id": 101, "name": "Erika", "is_active": True, "age": 45},
    {"id": 102, "name": "Marcus", "is_active": True, "age": 34},
    {"id": 103, "name": "David", "is_active": False, "age": 29},
    {"id": 104, "name": "Anna", "is_active": True, "age": 41.5},
    {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8},
]


@dataclass
class User:
    __slots__ = ["id", "name", "is_active", "age"]
    id: int
    name: str
    is_active: bool
    age: int

    def __post_init__(self):
        # simple validation
        if not isinstance(self.id, int):
            raise TypeError("'id' must be integer")
        if not isinstance(self.name, str):
            raise TypeError("'name' must be string")
        if not isinstance(self.is_active, bool):
            raise TypeError("'is_active' must be bool")
        if not isinstance(self.age, int):
            raise TypeError("'age' must be integer")


for row in USERS:
    User(**row)
