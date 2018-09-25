import json

from django.db import transaction

from notes_editor.models import Folder, Note


def create_folder(folder_name, user):
    folder_obj = Folder.objects.create(name=folder_name, user=user)
    print(folder_obj)
    return folder_obj


def rename_folder(folder_id, title, user):
    folder_obj = Folder.objects.get(id=folder_id)
    folder_obj.title = title

    return folder_obj


def get_all_folders():
    folders = Folder.objects.all()
    return json.dumps(folders)


def create_note(title, content, folder, user):
    note_obj = Note.objects.create({'title': title, 'content': content, 'folder': folder})
    return note_obj


@transaction.atomic
def edit_note(note_id, content, user):
    old_note_obj = Note.objects.filter(parent_note=note_id).filter(recent=1)[0]
    old_note_obj.recent = 0
    old_note_obj.save()
    note_obj = Note.objects.create({'title': old_note_obj.title, 'content': content, 'folder': old_note_obj.folder,
                                    'recent': 1, 'user': user})
    return note_obj


def rename_note(note_id, title, user):
    note_obj = Note.objects.filter(parent_note=note_id).filter(recent=1)[0]
    note_obj.title = title
    note_obj.save()
    return note_obj


def get_note_by_id(note_id):
    note = Note.objects.get(id=note_id)
    return json.dumps(note)


def get_all_folders_with_notes():
    hierarchy = {}
    folders = Folder.objects.values_list('id', flat=True)
    for folder in folders:
        notes = Note.objects.filter(folder=folder)
        hierarchy[folder] = notes
    return hierarchy


