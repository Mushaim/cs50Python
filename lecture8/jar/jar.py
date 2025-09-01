class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Only positive integers are allowed")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪"* self.size

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError("Not enough capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies")
        else:
            self._size -= n

    @property
    def capacity(self):
        if self._capacity < 0:
            raise ValueError("Only positive integers are allowed")
        return self._capacity

    @property
    def size(self):
        return self._size
