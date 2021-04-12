# import asyncio
# import json
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async

# from .models import Thread, ChatMessage


# class ChatConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         # when the socket is connected
#         print("connected", event)

#         await self.send({
#             'type': 'websocket.accept'
#         })

#         # await asyncio.sleep(5)

#         # await self.send({
#         #     'type': 'websocket.close'
#         # })
        
#         other_user = self.scope['url_route']['kwargs']['username']
#         me = self.scope['user']
#         thread_obj = await self.get_Thread(me, other_user)
#         self.thread_obj = thread_obj
#         chat_room = f"thread_{thread_obj.id}"
#         self.chat_room = chat_room
#         await self.channel_layer.group_add(
#             chat_room,
#             self.channel_name
#         )
#         # await self.send({
#         #     'type': 'websocket.send',
#         #     'text': {
#         #         'message': "msg test",
#         #         'username': "test"
#         #     }
#         # })
    
#     async def websocket_receive(self, event):
#         # when a message is received from websocket
#         print("receive", event)
#         # receive {'type': 'websocket.receive', 'text': '{"message":"test"}'}
#         front_text = event.get('text', None)
#         if front_text is not None:
#             loaded_dict_data = json.loads(front_text)
#             msg = loaded_dict_data.get('message', None)
#             user = self.scope['user']
#             username =  'default'
#             if user.is_authenticated:
#                 username = user.username
#                 await self.create_chat_message(user, msg)
#             myResponse = {
#                 'message': msg,
#                 'username': username
#             }

#             # brodcasts the message event to be sent
#             await self.channel_layer.group_send(
#                 self.chat_room,
#                 {
#                     "type": "chat_message",
#                     "text": json.dumps(myResponse),
#                 }
#             )

#     async def chat_message(self, event):
#         # send the actual message
#         await self.send({
#             'type': 'websocket.send',
#             'text': event['text']
#         })
    
#     async def websocket_disconnect(self, event):
#         # when the socket is disconnected
#         print("disconnect", event)

#     @database_sync_to_async
#     def get_Thread(self, user, other_user):
#         return Thread.objects.get_or_new(user, other_user)[0]

#     @database_sync_to_async
#     def create_chat_message(self, me, msg):
#         return ChatMessage.objects.create(thread=self.thread_obj, user=me, message=msg)



# class jokesConsumer(AsyncConsumer):
    # async def websocket_connect(self, event):
    #     # when the socket is connected
    #     print("connected", event)
    #     await self.channel_layer.group_add(
    #         'jokes',
    #         self.channel_name
    #     )

    # async def websocket_receive(self, event):
    #     # when a message is received from websocket
    #     print("receive", event)

    #     await self.send({
    #         'type': 'websocket.send',
    #         'text': 'instant message'
    #     })


    # async def send_jokes(self, event):
    #     print("event12", event)
    #     # text_messgae = event['text']

    #     await self.send({
    #         'type': 'websocket.send',
    #         'text': event['text']
    #     })

    # async def websocket_disconnect(self, event):
    #     # when the socket is disconnected
    #     print("disconnect", event)

from channels.generic.websocket import AsyncWebsocketConsumer

class jokesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    async def disconnect(self):
        print("disconnected")
        await self.channel_layer.group_discard('jokes', self.channel_name)


    async def send_jokes(self, event):
        print("eventTest", event)
        await self.send(event['text'])