#!/usr/bin/python3
'''Contains the unique file storage instance for our application'''
from .engine.file_storage import FileStorage

__all__ = ["BaseModel"]

storage = FileStorage()
storage.reload()
