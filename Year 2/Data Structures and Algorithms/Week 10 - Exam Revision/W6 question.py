

class Queue:
    def __init__(new_queue):
        new_queue._contents = []

    def enqueue(queue, value):
        queue._contents.append(value)

    def front(queue):
        return queue._contents[0]

    def dequeue(queue):
        front = queue.front()
        del queue._contents[0]
        return front

    def count(queue):
        return len(queue._contents)

    # Just so we can print a queue
    def __str__(queue):
        # Just change bracket appearance to <---<
        return f"<{str(queue._contents)[1:-1]}<"

    def __repr__(queue):
        return str(queue)

## swap the first two elements in a queue
def swap(q):
    ## base case, if less than 2 return because will forever be the same
    if q.count() < 2:
        return q
    # make a new queue
    new_queue = Queue()
    # Store the first element which is dequeued from the queue
    first = q.dequeue()
    # second element dequeued from the queue
    second = q.dequeue()

    # Swap the first two elements
    new_queue.enqueue(second)
    new_queue.enqueue(first)

    while q.count() > 0:
        new_queue.enqueue(q.dequeue())

    return new_queue





def same(q):
    if q.count() == 0:
        return False

    first = q.front()
    last = None
    temp_queue = Queue()

    while q.count() > 0:
        last = q.dequeue()
        temp_queue.enqueue(last)

    while temp_queue.count() > 0:
        q.enqueue(temp_queue.dequeue())

    return first == last



## Testing
q = Queue()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(2)

print("Original queue:", q)

# Swap operation
swapped_queue = swap(q)
print("Swapped queue:", swapped_queue)

# Same operation
is_same = same(q)
print("Are the first and last elements the same?", is_same)
