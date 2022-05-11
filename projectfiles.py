# Project Files Handling

def open_files():
    try:
        chapter_summary_FILE = open("rawfiles/chaptersummaries.txt").readlines()

    except:
        print("File Import Error")
    