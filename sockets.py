import socketio
import asyncio
import time
active_sessions = {}

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)


@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    active_sessions[sid] = True
    await sio_server.emit('join', {'sid': sid})


# @sio_server.event
# async def chat(sid, message):
#     await sio_server.emit('chat', {'sid': sid, 'message': message})

@sio_server.on('join1')
async def handle_join(sid, *args, **kwargs):
    count = 1
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here {count} and sid is {sid}"
        await sio_server.emit('countData',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count here {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join2')
async def handle_join2(sid, *args, **kwargs):
    count = 90971
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here2 {count} and sid2 is {sid}"
        await sio_server.emit('countData2',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count2 here {val} ')

@sio_server.on('join3')
async def handle_join3(sid, *args, **kwargs):
    count = 7891
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here3 {count} and sid is {sid}"
        await sio_server.emit('countData3',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count3 here {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join4')
async def handle_join4(sid, *args, **kwargs):
    count = 1561
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data her42 {count} and sid2 is {sid}"
        await sio_server.emit('countData4',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count4 here {val} ')

@sio_server.on('join5')
async def handle_join5(sid, *args, **kwargs):
    count = 123
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here5 {count} and sid is {sid}"
        await sio_server.emit('countData5',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count5 here {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join6')
async def handle_join6(sid, *args, **kwargs):
    count =991
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here6 {count} and sid2 is {sid}"
        await sio_server.emit('countData6',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count6 here {val} ')

@sio_server.on('join7')
async def handle_join7(sid, *args, **kwargs):
    count = 354671
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here7 {count} and sid is {sid}"
        await sio_server.emit('countData7',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count here7 {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join8')
async def handle_join8(sid, *args, **kwargs):
    count = 1
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here8 {count} and sid2 is {sid}"
        await sio_server.emit('countData8',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count8 here {val} ')

@sio_server.on('join9')
async def handle_join9(sid, *args, **kwargs):
    count = 4651
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here9 {count} and sid is {sid}"
        await sio_server.emit('countData9',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count here9 {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join10')
async def handle_join10(sid, *args, **kwargs):
    count = 165
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here10 {count} and sid2 is {sid}"
        await sio_server.emit('countData10',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count2 here10 {val} ')


@sio_server.on('join11')
async def handle_join11(sid, *args, **kwargs):
    count = 109
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here11 {count} and sid is {sid}"
        await sio_server.emit('countData11',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count here11 {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join12')
async def handle_join12(sid, *args, **kwargs):
    count =81
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here12 {count} and sid2 is {sid}"
        await sio_server.emit('countData12',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count12 here {val} ')

@sio_server.on('join13')
async def handle_join13(sid, *args, **kwargs):
    count = 18
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here13 {count} and sid is {sid}"
        await sio_server.emit('countData13',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count here13 {val} ')
        # if count % 20 == 0:
        #     print(f"exited ... {val}")
        #     await asyncio.sleep(10 * 60)
@sio_server.on('join14')
async def handle_join14(sid, *args, **kwargs):
    count = 9
    while active_sessions.get(sid, False):
    # while True:

        val = f"total data here14 {count} and sid2 is {sid}"
        await sio_server.emit('countData14',val)
        count +=1
        await asyncio.sleep(0.0002)
        print(f'val count14 here {val} ')                                        

@sio_server.on('test')
async def test(sid, *args, **kwargs):
    await sio_server.emit('hey', 'joe')

@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')
    active_sessions[sid] = False
