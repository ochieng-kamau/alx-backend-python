#!/usr/bin/env python3
''' Description: asynchronous coroutine wait_random taking in an argument
                 (max_delay) that waits for a random delay between 0 and 
                 max_delay seconds and finally returns it
    Arguments: max_delay: int = 10
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay seconds and then return the delay. '''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
