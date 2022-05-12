# Project Files Handling

import keyboard


print("test")

file_names = ("rawfiles/chaptersummaries.txt")

def open_files():
    try:
        chapter_summary_FILE = open().readlines()
        print("rawfiles/chaptersummaries.txt successfully loaded")
    except:
        print("File Import Error")
    
