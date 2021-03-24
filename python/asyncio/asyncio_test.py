import asyncio
import random

# Example of Coroutine function

async def main(): 
    print("Hello ...")
    await asyncio.sleep(1)
    print('... World.')

asyncio.run(main())


# Example of awaiting and printing Coroutine object

async def return_randint():
    return random.randint(0,9)

async def main_2():
    # return_randint()
    print(await return_randint())

asyncio.run(main_2())