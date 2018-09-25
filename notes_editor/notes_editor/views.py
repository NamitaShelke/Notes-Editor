import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from notes_editor.utils import create_folder, create_note, edit_note, get_all_folders_with_notes, rename_note, \
    rename_folder


def register(request):
    """
    register the user
    """
    if request.method == 'POST':
        t = loader.get_template('login.html')
        json_obj = json.loads(request.body.decode(encoding='UTF-8'))
        username = json_obj.get('username')
        password = json_obj.get('password')
        email = json_obj.get('email')
        User.objects.create_user(username=username, password=password, email=email)
        return HttpResponseRedirect('/login')


def display_homepage(request):
    """
    display the folder and notes hierarchy
    """
    t = loader.get_template('home.html')
    return HttpResponse(t.render())


@login_required
@csrf_exempt
def create_folder_view(request):
    """
    Create the folder
    """
    if request.method == 'POST':
        user = request.user
        print(user)
        json_obj = json.loads(request.body.decode(encoding='UTF-8'))
        print(json_obj)
        folder_name = json_obj.get('folder_name')
        create_folder(folder_name, user)
        return HttpResponse(json.dumps({'status': True}), 'json')


@login_required
def rename_folder_view(request):
    """
    Rename the notes folder
    """
    if request.method == 'POST':
        user = request.user
        json_obj = json.loads(request.body.decode(encoding='UTF-8'))
        folder_id = json_obj.get('folder_id')
        folder_new_name = json_obj.get('folder_new_name')
        rename_folder(folder_id, folder_new_name, user)
        return HttpResponseRedirect('/home')


@login_required
def create_note_view(request):
    """
    Create the note
    """
    if request.method == 'POST':
        user = request.user
        json_obj = json.loads(request.body.decode(encoding='UTF-8'))
        note_title= json_obj.get('title')
        content = json_obj.get('content')
        folder = json_obj.get('folder')
        create_note(note_title, content, folder, user)
        return HttpResponseRedirect('/home')


@login_required
def edit_note_view(request):
    """
    Edit the note
    """
    if request.method == 'POST':
        user = request.user
        json_obj = json.loads(request.body.decode(encoding='UTF-8'))
        note_title= json_obj.get('title')
        content = json_obj.get('content')
        folder = json_obj.get('folder')
        edit_note(note_title, content, folder, user)
        return HttpResponseRedirect('/home')


@login_required
def rename_note_view(request):
    """
    Rename the notes title
    """
    if request.method == 'POST':
        user = request.user
        json_obj = json.loads(request.body.decode(encoding='UTF-8'))
        note_id = json_obj.get('folder_id')
        note_new_name = json_obj.get('folder_new_name')
        rename_note(note_id, note_new_name, user)
        return HttpResponseRedirect('/home')