from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    name = models.CharField(max_length=191, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'folder'
        app_label = 'notes_editor'


class Note(models.Model):
    title = models.CharField(max_length=191)
    parent_note = models.ForeignKey("Note", default=id, on_delete=models.CASCADE)
    content = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recent = models.BooleanField(default=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notes'
        app_label = 'notes_editor'



