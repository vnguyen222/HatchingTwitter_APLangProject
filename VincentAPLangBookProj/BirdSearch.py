''' HATCHING TWITTER AP LANGUAGE FINAL PROJECT '''
''' BY: VINCENT NGUYEN '''
import backend

import time

# Clearing terminal
import os, platform
def CLEAR_TERMINAL():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
# Window Sizing Handling
def window_size():
    raw_terminal_size = str(os.get_terminal_size())
    size_numbers = raw_terminal_size[25:]
    size = []
    numtostr = ""
    for x in size_numbers:
        if x.isdigit():
            numtostr += x
        else:
            if len(numtostr) > 0:
                size.append(int(numtostr))
                numtostr = ""

    return size
        

# Print Effect Function
def print_effect(str, delay):
    for x in str:
        print(x, end="")
        time.sleep(delay)

# Twitter ASCII Logo Tuple
twitter_ASCII_logo = (
        "                                                    (((((((()                                     ",
        "                              /                    ((((((((((/  .(/,                              ",
        "                             ((((,               ((((((((((((((((. .(                             ",
        "                             /(((((((           ((((((((((((((((((/                               ",
        "                              ((((((((((((,     (((((((((((((((((                                 ",
        "                             .  (((((((((((((((((((((((((((((((((                                 ",
        "                             ,((((((((((((((((((((((((((((((((((*                                 ",
        "                               (((((((((((((((((((((((((((((((((                                  ",
        "                                 /(((((((((((((((((((((((((((((                                   ",
        "                                 (((((((((((((((((((((((((((((                                    ",
        "                                  ,((((((((((((((((((((((((/                                      ",
        "                                        ((((((((((((((((((                                        ",
        "                                   ,((((((((((((((((((/.                                          ",
        "                              //(((((((((((((((((((,                                              ")
# Special Characters Not Allowed in Search
special_characters = "[@_!#$%^&*()<>/\|}{~:]"

def loading_screen():
    CLEAR_TERMINAL()
    print(platform.system(), platform.version(), platform.architecture(), "\nPython", platform.python_version(), platform.python_implementation(), platform.python_compiler(), end="\n\n")
    backend.open_files()
    time.sleep(1)
    CLEAR_TERMINAL()

def search_screen():
    CLEAR_TERMINAL()
    print("--------------")
    print("| BirdSearch |    A search for information about the creation of Twitter")
    print("--------------")
    for l in twitter_ASCII_logo:
        time.sleep(0.05)
        print(l)
    print("#QUIT to exit")
    while True:
        # Get user search input
        search_query_preparsed = input("\nSearch: ")
        # Exit Command
        if search_query_preparsed == "#QUIT":
            CLEAR_TERMINAL()
            print("Exiting...")
            exit()
        search_query_preparsed = search_query_preparsed.lower()
        query_valid = True

        # Search Checking
        for x in search_query_preparsed:    # Checking if any digits or illegal symbols in the string
            if x.isdigit():
                query_valid = False
                break
            for sym in special_characters:
                if x == sym:
                    query_valid = False
                    break

        # Question Mark Handling
        if "?" in search_query_preparsed:
            search_query_preparsed = search_query_preparsed.replace("?", "")

        if query_valid:
            return search_query_preparsed.split()
        else:
            print ("Enter a valid search")



# EXECUTE MAIN
if __name__ == "__main__":
    loading_screen()

    #backend.print_result("#summary", "rawfiles/chaptersummaries.txt", window_size())
    
    while True:
        search_query = search_screen()
        result_file = None
        try:
            result_file = backend.result_file(search_query)
        except Exception as e:
            print("No results found")
            time.sleep(2.5)
        else:
            backend.print_result(search_query, result_file, window_size())
    