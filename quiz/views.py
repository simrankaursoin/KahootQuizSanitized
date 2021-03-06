
# Create your views here.
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'quiz/index.html', {})


def room(request, room_name, user_name):
    return render(request, 'quiz/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user_name_json': mark_safe(json.dumps(user_name)),
    })


def teacher_room(request, room_name, user_name):
    return render(request, 'quiz/teacher.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user_name_json': mark_safe(json.dumps(user_name)),
    })


def bargraph_display(request, room_name, user_name):
    return render(request, 'quiz/bargraph.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'user_name_json': mark_safe(json.dumps(user_name)),
    })
