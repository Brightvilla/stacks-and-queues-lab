import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        return self.items.pop(0) if not self.is_empty() else None

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        winner = random.choice(self.items)

        # Dequeue until we remove the winner
        while True:
            removed = self.dequeue()
            if removed == winner:
                break

        return winner