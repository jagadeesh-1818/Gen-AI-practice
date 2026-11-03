from typing import TypedDict

class Person (TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'Jagadeesh', 'age': 22}

print(new_person)