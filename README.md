# Stacks and Queues Lab

A Python lab implementing a **parentheses validator** using a stack and a **customer raffle system** using a queue.

---

## Project Structure

```
stacks-and-queues-lab/
├── custom_stack.py       # Stack-based parentheses validator
├── custom_queue.py       # Queue class with raffle winner logic
├── test_structures.py    # Unit tests
└── README.md
```

---

## How to Run

### Run Tests
```bash
python test_structures.py
```

### Requirements
- Python 3.x (no external dependencies)

---

## Features

### Stack — `custom_stack.py`
- `is_valid_parentheses(s: str) -> bool` — Returns `True` if `()`, `{}`, and `[]` are balanced in the string.

### Queue — `custom_queue.py`
- `enqueue(item)` — Add item to the back
- `dequeue()` — Remove and return item from the front
- `peek()` — View front item without removing
- `is_empty()` — Check if queue is empty
- `select_and_announce_winner()` — Randomly picks a winner and dequeues all entries up to and including them

---

## Concepts

| Structure | Behavior | Use Case |
|-----------|----------|----------|
| Stack     | LIFO     | Parentheses validation |
| Queue     | FIFO     | Customer raffle system |
