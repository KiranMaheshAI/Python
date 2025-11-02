# asyncio.Queue() in Python provides an asynchronous, thread-safe, and first-in, first-out (FIFO) queue specifically designed for use within asyncio applications. It enables synchronized communication and data exchange between different coroutines. 
# Key characteristics and usage: 

# • Asynchronous Operations: The put() and get() methods of asyncio.Queue are awaitable. This means a coroutine attempting to get() an item from an empty queue will pause its execution until an item becomes available, without blocking the entire event loop. Similarly, a put() operation on a full queue (if a maxsize was specified) will also await until space becomes available. 
# • Synchronization Primitive: It acts as a crucial synchronization primitive, allowing producer coroutines to add items to the queue and consumer coroutines to retrieve them in a coordinated manner. 
# • maxsize Parameter: When creating an asyncio.Queue, an optional maxsize argument can be provided. This limits the number of items the queue can hold, preventing unbounded memory consumption. If maxsize is 0 (the default), the queue size is unlimited. 
# • Methods: 
# 	• await put(item): Adds an item to the queue. If the queue is full (and maxsize is set), this operation will await until space is available. 
# 	• await get(): Removes and returns an item from the queue. If the queue is empty, this operation will await until an item is available. 
# 	• qsize(): Returns the current number of items in the queue. 
# 	• empty(): Returns True if the queue is empty, False otherwise. 
# 	• full(): Returns True if the queue is full (based on maxsize), False otherwise. 

import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(0.1) # Simulate some work
        await queue.put(f"Item {i}")
        print(f"Produced: Item {i}")

async def consumer(queue, consumer_id):
    while True:
        item = await queue.get()
        print(f"Consumer {consumer_id} consumed: {item}")
        queue.task_done() # Indicate that a retrieved task has been processed

async def main():
    queue = asyncio.Queue(maxsize=3) # Create a queue with a max size
    producers = [asyncio.create_task(producer(queue))]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(2)]

    await asyncio.gather(*producers) # Wait for producers to finish
    await queue.join() # Wait until all items in the queue have been processed
    for c in consumers:
        c.cancel() # Cancel consumer tasks

if __name__ == "__main__":
    asyncio.run(main())