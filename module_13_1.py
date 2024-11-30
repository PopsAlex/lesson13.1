import asyncio

async def start_strongman(name, power, amt_bolls = 5):
    print(f'Силач {name} начал соревнования')
    for i in range(amt_bolls):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1} шар')

    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Лёха', 3))
    task2 = asyncio.create_task(start_strongman('Андрюха', 4))
    task3 = asyncio.create_task(start_strongman('Бартоломей', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())