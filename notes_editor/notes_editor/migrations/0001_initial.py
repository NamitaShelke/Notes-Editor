# Generated by Django 2.1.1 on 2018-09-23 19:37

import builtins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=191)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'folder',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191)),
                ('content', models.TextField(default='')),
                ('recent', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes_editor.Folder')),
                ('parent_note', models.ForeignKey(default=builtins.id, on_delete=django.db.models.deletion.CASCADE, to='notes_editor.Note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notes',
            },
        ),
    ]
