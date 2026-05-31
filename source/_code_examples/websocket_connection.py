import asyncio      # builtin
import websockets   # pip install websockets

WEBSOCKET_URL = "https://my-kindafax-instance.example.com"

async def main():

    # Open a connection, with a context handler.
    async with websockets.connect(WEBSOCKET_URL) as websocket:

        # Send a message to the server.
        await websocket.send("Hello World!")

        # Wait for a response back.
        response = await websocket.recv()
        print(response) # Print the response to the console


# Run asynchronously using asyncio
asyncio.run(main())