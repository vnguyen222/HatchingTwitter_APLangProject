# Project Files Handling

import keyboard


chapter_summary_FILE = None

FILE_LOCATIONS = ("rawfiles/chaptersummaries.txt", "rawfiles/timeline.txt")
files = (chapter_summary_FILE)

def open_files():
    for i in range(0, len(FILE_LOCATIONS)):
        try:
            files[i] = open(FILE_LOCATIONS[i])
        except:
            print("File", FILE_LOCATIONS[i], "Import Error")

def print_result(screen_width, screen_height, file):
    for x in range(0, screen_width):
        print("-", end="")
    
