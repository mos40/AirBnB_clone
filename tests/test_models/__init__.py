#!/usr/bin/python3
"""Initialization magic method for models directory"""
from models.engine.file_storage import FileStorage


# Create an instance of FileStorage and load data
storage_instance = FileStorage()
storage_instance.reload()
