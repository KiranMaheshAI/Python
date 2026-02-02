import time
import asyncio

async def brew_coffee():
    print("Brewing coffee...")
    await asyncio.sleep(3)
    print("Coffee brewed")
    return "Coffee"

async def toast_bread():
    print("Toasting bread...")
    await asyncio.sleep(10)
    print("Bread toasted")
    return "Bread"

# One way of calling async functions
async def main():
    start = time.time()
    bread_task = asyncio.create_task(toast_bread())
    coffee_task = asyncio.create_task(brew_coffee())
    print("Waiting for coffee to brew...")
    coffee = await coffee_task
    print(f"Sample Time taken")
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    bread = await bread_task
    print(f"Coffee1: {coffee}")
    print(f"Bread1: {bread}")
    print(f"Time taken: {end - start} seconds")


# Another way of calling async functions
async def main2():
    start = time.time()
    asyncio.gather(brew_coffee(), toast_bread())
    print(f"Sample Time taken")
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    await asyncio.sleep(4)  # Wait enough time for tasks to complete
    await asyncio.sleep(10)


async def main3():
    start = time.time()
    coffee = await brew_coffee()
    toast = await toast_bread()
    asyncio.gather(coffee, toast)
    print(f"Sample Time taken")
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    await asyncio.sleep(4)  # Wait enough time for tasks to complete
    await asyncio.sleep(10)

if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(main3())