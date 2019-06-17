
# Create your views here.
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'quiz/index.html', {})


def room(request, room_name):
    print("in wrong view")
    return render(request, 'quiz/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def teacher_room(request, room_name):
    print("in correct view")
    return render(request, 'quiz/teacher.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
