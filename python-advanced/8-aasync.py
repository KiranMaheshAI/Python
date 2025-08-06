import time
import asyncio
async def brew_coffee():
    print("Brewing coffee...")
    await asyncio.sleep(3)
    print("Coffee brewed")
    return "Coffee"

async def toast_bread():
    print("Toasting bread...")
    await asyncio.sleep(2)
    print("Bread toasted")
    return "Bread"
# One way of calling async functions
async def main():
    start = time.time()
    coffee_task = asyncio.create_task(brew_coffee())
    bread_task = asyncio.create_task(toast_bread())
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
    await asyncio.gather(brew_coffee(), toast_bread())
    end = time.time()
    print(f"Time taken: {end - start} seconds")

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main2())