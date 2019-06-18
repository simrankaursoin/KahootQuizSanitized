# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import random


class QuizConsumer(WebsocketConsumer):

    def release_new_question(self):
        question = "New question from " + self.user_name + ": " + str(random.randint(1, 100))
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'question_message',
                'question': question,
            }
        )

    def send_connected_message(self):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'connected_message',
                'name': self.user_name,
            }
        )

    def display_bargraph(self):
        print("display_bargraph")

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        self.room_group_name = 'quiz_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send_connected_message()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if 'next_question' in text_data_json:
            self.release_new_question()
        # Send message to room group
        elif 'display_bargraph' in text_data_json:
            self.display_bargraph()
        else:
            message = text_data_json['message']
            student_answer = message.split(":")[1].strip()
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

    def connected_message(self, event):
        name = event['name']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'name': name,
        }))