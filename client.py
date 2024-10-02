import asyncio

import socketio

sio_client = socketio.AsyncClient()


@sio_client.event
async def connect():
    print('I\'m connected')


@sio_client.event
async def disconnect():
    print('I\'m disconnected')


async def main():
    print("the client is called here 123424234234232134")
    await sio_client.connect(url='http://localhost:5000', socketio_path='sockets')
    await sio_client.disconnect()

asyncio.run(main())
