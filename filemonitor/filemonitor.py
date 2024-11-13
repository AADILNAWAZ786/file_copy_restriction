import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import pyperclip
from django.conf import settings

# Load the root folder from Django settings or database
ROOT_FOLDER = settings.ROOT_FOLDER

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        self.check_file_restriction(event.src_path)
    
    def on_created(self, event):
        if event.is_directory:
            return
        self.check_file_restriction(event.src_path)

    def check_file_restriction(self, file_path):
        if not file_path.startswith(ROOT_FOLDER):
            print(f"Attempt to copy file outside the root folder: {file_path}")
            os.remove(file_path)  # Delete file that is copied outside the allowed folder
    
    def on_moved(self, event):
        if event.is_directory:
            return
        self.check_file_restriction(event.dest_path)

def start_file_monitor():
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=ROOT_FOLDER, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

