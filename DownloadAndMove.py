import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/gopui/OneDrive/Pictures"
to_dir = "E:/GOURI/pictures"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif', '.webp'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        print(event)
        print(event.src_path)

        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        print(name, extension)

        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                
                filename = os.path.basename(event.src_path)

                src = "C:/Users/gopui/OneDrive/Pictures/" + filename

                dest = "E:/GOURI/pictures/" + filename

                if (os.path.exists(dest)):
                    print("exists")

                    new_filename = os.path.splitext(filename)[0]+ str(random.randint(0,999)) + os.path.splitext(filename)[1]
                    print(new_filename)

                    dest = "E:/GOURI/pictures/" + new_filename
                    

                shutil.move(src, dest)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
while True:
    time.sleep(5)
    print("running...")

    
