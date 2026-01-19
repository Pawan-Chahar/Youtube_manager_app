import asyncio 
import time 
import aiohttp 
import requests 
from icecream import ic # print

# Async GOOD -> Web requests, File Reading, DB Queries, API Calls, Any I/O Operation

# Async BAD -> Math stuff , Image Processing , CPU Intense Work

def sync_requests():
    print("Making slow requests...")
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1"
    ]
    
    start = time.time()
    for i, url in enumerate(urls):
        ic(f"Request {i+1}: starting")
        r = requests.get(url)
        ic(f"Request {i+1}: done")

    total = time.time() - start 
    ic(f"Total time: {round(total,1)} seconds")
    print()


# Basic Async Example 
# async await 
async def async_starter():
    print("Basic Starter Example")

    async def do_work(name:str, secs:int) -> str:
        ic(f"{name} starting")
        await asyncio.sleep(1)
        ic(f"{name} finished")
        return f"{name} Done!"
    
    # All run at the same time 
    task1 = asyncio.create_task(do_work("Like", 2))
    task2 = asyncio.create_task(do_work("Comment", 1))
    task3 = asyncio.create_task(do_work("Subscribe", 1.5))


    results = await asyncio.gather(task1, task2, task3)
    ic(f"Results: {results}")
    print()





async def main():
    sync_requests()

    await async_starter()

if __name__ == "__main__":
    asyncio.run(main())
