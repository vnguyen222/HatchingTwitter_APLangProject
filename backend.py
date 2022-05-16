# Project Files Handling

import keyboard, time, os

def CLEAR_TERMINAL():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


FILE_LOCATIONS = ("rawfiles/chaptersummaries.txt", "rawfiles/timeline.txt", "rawfiles/summary.txt", "rawfiles/reflection.txt", "rawfiles/aboutodeo.txt", "rawfiles/abouttwitter.txt", "rawfiles/ceos.txt")
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
    elif "reflection" in search:
        return FILE_LOCATIONS[3]
    elif "what" in search and "is" in search and "twitter" in search:
        return FILE_LOCATIONS[5]
    elif "ceo" in search:
        return FILE_LOCATIONS[6]
    else:
        raise Exception("No results found")



def open_files():
    for i in range(0, len(FILE_LOCATIONS)):
        try:
            FILES.append(open(FILE_LOCATIONS[i]))
        except Exception as e:
            print("File", FILE_LOCATIONS[i], "Import ERROR")
            print(e)
        else:
            print(FILE_LOCATIONS[i], "successfully imported")

def print_result(search, filename, screen_dimensions):
    index = FILE_LOCATIONS.index(filename)
    file = FILES[index].readlines()
    start, end = 0, screen_dimensions[1]-14
    while True:
        CLEAR_TERMINAL()
        print("Showing results for:", search)
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

        while True:
            if keyboard.is_pressed('q'):
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


# Search Query Handling

COMMON_QUESTION_WORDS = ("what", "where", "who", "why")

def mispelled_similar(base_word, user_word):
    if abs(len(user_word) - len(base_word)) < 2:
        return False




def parse_query(user_search):
    search = None
    if user_search[0] == "#":
        search = [user_search[1:]]
    else:
        search = user_search.split()

    return result_file(search)

    '''
    for q_word in COMMON_QUESTION_WORDS:
        if search[0] == q_word or :'''