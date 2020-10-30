import asyncio
# Automatically handles sending json objects
from channels.generic.websocket import AsyncJsonWebsocketConsumer

# class EchoConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         await self.send({
#             "type": "websocket.accept"
#         })
    
#     async def websocket_receive(self, event):
#         #Echo the recieved payload
#         #sending something over a client network is a blocking activity
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"]
#         })


class TickTockConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while 1:
            await asyncio.sleep(1)
            await self.send_json("tick")
            await asyncio.sleep(1)
            await self.send_json(".......tock")