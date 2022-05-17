from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class SightsIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse = False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class SightsCollection(Iterable):
    def __init__(self, collection = []):
        self._collection = collection

    def __iter__(self):
        return SightsIterator(self._collection)

    def get_reverse_iterator(self):
        return SightsIterator(self._collection, True)

    def add_sight(self, item):
        self._collection.append(item)


if __name__ == "__main__":

    paris = SightsCollection()
    paris.add_sight('Panthéon')
    paris.add_sight('Place de la Concorde')
    paris.add_sight('Pont Alexandre III')
    paris.add_sight('Jardin du Luxembourg')
    paris.add_sight('Cathédrale Notre-Dame')
    print("Paris")
    print("//".join(paris))

    print("Paris reversed")
    print("//".join(paris.get_reverse_iterator()))
