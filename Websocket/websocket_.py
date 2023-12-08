#!/usr/bin/env python
import asyncio

from websockets.exceptions import ConnectionClosedError
import websockets



async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()

            print('Incoming message | ', message)
        except ConnectionClosedError as err:
            print(f"{err} type error: {type(err)}")
        except Exception as new_err:
            print(f"{new_err} type error: {type(new_err)}")


async def main():
    async with websockets.serve(handler, "", 8011):
        await asyncio.Future()  # run forever

# py -m websockets ws://localhost:8011/
# py -m websocket_

if __name__ == "__main__":
    asyncio.run(main())


