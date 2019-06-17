# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class QuizConsumer(WebsocketConsumer):
    def release_new_question(self):
        question = "new_question!"
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'question_message',
                'question': question,
            }
        )

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'quiz_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.release_new_question()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'quiz_message',
                'message': message,
            }
        )

    # Receive message from room group
    def quiz_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
        }))

    def question_message(self, event):
        question = event['question']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'question': question,
        }))