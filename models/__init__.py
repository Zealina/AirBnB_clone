#!/usr/bin/python3
"""
Create a Unique 'FileStorage' instance for the Application
"""

from engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
