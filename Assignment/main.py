from stack_ds import Stack
from queue_ds import Queue

# Create instances
my_stack = Stack(7)
my_stack.push(4)
my_stack.push(9)

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Initial Stack:")
my_stack.print_stack_items()
print("\nInitial Queue:")
my_queue.print_queue_items()

# Pop from stack to queue
print("\n--- Pop from stack to queue ---")
my_stack.pop_to_queue(my_queue)

print("\nStack after pop:")
my_stack.print_stack_items()
print("\nQueue after enqueue:")
my_queue.print_queue_items()

# Dequeue from queue to stack
print("\n--- Dequeue from queue to stack ---")
my_queue.dequeue_to_stack(my_stack)

print("\nStack after push:")
my_stack.print_stack_items()
print("\nQueue after dequeue:")
my_queue.print_queue_items()