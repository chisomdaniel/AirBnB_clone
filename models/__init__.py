#!/usr/bin/python3
"""Contains the unique file storage instance for our application"""

from models.engine.file_storage import FileStorage

from .engine.file_storage import FileStorage
from models import base_model

storage = FileStorage()
storage.reload()
