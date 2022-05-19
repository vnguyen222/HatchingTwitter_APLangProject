# Project Files Handling

import keyboard, time, os, sys

def CLEAR_TERMINAL():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


FILE_LOCATIONS = ("rawfiles/chaptersummaries.txt", "rawfiles/timeline.txt", "rawfiles/summary.txt", "rawfiles/reflection.txt", "rawfiles/whatodeo.txt", "rawfiles/whattwitter.txt", "rawfiles/ceos.txt", "rawfiles/analysis.txt", "rawfiles/iraq.txt", "rawfiles/founded.txt", "rawfiles/informationproj.txt", "rawfiles/firsttweet.txt", "rawfiles/offered.txt", "rawfiles/outted.txt", "rawfiles/celebrities.txt")
FILES = []

def result_file(search):
    if "chapter" in search and "summary" in search:
        return FILE_LOCATIONS[0]
    elif "summary" in search:
        return FILE_LOCATIONS[2]
    elif "what" in search and "odeo" in search:
        return FILE_LOCATIONS[4]
    elif "timeline" in search:
        return FILE_LOCATIONS[1]
    elif "reflection" in search and "vincent's":
        return FILE_LOCATIONS[3]
    elif "iraq" in search:
        return FILE_LOCATIONS[8]
    elif "what" in search and "twitter" in search:
        return FILE_LOCATIONS[5]
    elif "kicked" in search:
        return FILE_LOCATIONS[13]
    elif "ceo" in search or "ceos" in search:
        return FILE_LOCATIONS[6]
    elif "analysis" in search:
        return FILE_LOCATIONS[7]
    elif "founded" in search:
        return FILE_LOCATIONS[9]
    elif "information" in search and "project" in search:
        return FILE_LOCATIONS[10]
    elif "first" in search and "tweet" in search:
        return FILE_LOCATIONS[11]
    elif "purchase" in search:
        return FILE_LOCATIONS[12]
    elif "celebrities" in search:
        return FILE_LOCATIONS[14]
    else:
        raise Exception("No results found")


def open_files():
    for i in range(0, len(FILE_LOCATIONS)):
        try:
            FILES.append(open(FILE_LOCATIONS[i]).readlines())
        except Exception as e:
            print("File", FILE_LOCATIONS[i], "Import ERROR")
            print(e)
        else:
            print(FILE_LOCATIONS[i], "successfully imported")

def print_result(search, filename, screen_dimensions):
    index = FILE_LOCATIONS.index(filename)
    file = FILES[index]
    start, end = 0, screen_dimensions[1]-14
    while True:
        CLEAR_TERMINAL()
        print("Showing results for: ", end="")
        for word in search:
            print(word, end=" ")
        print()
        for x in range(0, screen_dimensions[0]):
            print("-", end="")
        print()
        
        if len(file) < screen_dimensions[1]-14:
            for x in file[start:]:
                print(x, end="")
        else:
            for x in file[start:end]:
                print(x, end="")
        print()

        print("--[Quit: q]--[Scroll: ↑↓]--", end="")
        for x in range(27, screen_dimensions[0]):
            print("-", end="")
        print("")

        # Keybinds for actions
        while True:
            if keyboard.is_pressed('q'):
                sys.stdin.flush()
                return
            if keyboard.is_pressed("up arrow"):
                if start > 0:
                    start -= 1
                    end -= 1
                    time.sleep(0.01)
                    break
            if keyboard.is_pressed("down arrow"): 
                if end < len(file):
                    start += 1
                    end += 1
                    time.sleep(0.01)
                    break