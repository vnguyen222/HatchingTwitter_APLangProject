''' HATCHING TWITTER AP LANGUAGE FINAL PROJECT '''
''' BY: VINCENT NGUYEN '''
import projectfiles, searchhandling

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
    size = os.get_terminal_size()

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
special_characters = "[@_!#$%^&*()<>?/\|}{~:]"

def loading_screen():
    CLEAR_TERMINAL()
    print(platform.system(), platform.version(), platform.architecture(), "\nPython", platform.python_version(), platform.python_implementation(), platform.python_compiler(), end="\n\n")
    projectfiles.open_files()
    time.sleep(1)
    CLEAR_TERMINAL()

def search_screen():
    CLEAR_TERMINAL()
    print("--------------")
    print("| BirdSearch |")
    print("--------------")
    for l in twitter_ASCII_logo:
        time.sleep(0.05)
        print(l)
    while True:
        # Get user search input
        search_query_preparsed = input("\nSearch: ")
        search_query_preparsed = search_query_preparsed.lower()
        query_valid = True

        # Search Checking
        if search_query_preparsed[0] == "#" and search_query_preparsed.index(" ") < 0:  # Short search
            return search_query_preparsed

        for x in search_query_preparsed:    # Checking if any digits or illegal symbols in the string
            if x.isdigit():
                query_valid = False
                break
            for sym in special_characters:
                if x == sym:
                    query_valid = False
                    break

        if query_valid:
            return search_query_preparsed
        else:
            print ("Enter a valid search")

def result_screen(user_search, requested_file):
    CLEAR_TERMINAL()
    print("Showing results for:", user_search)
    
    


# EXECUTE MAIN
if __name__ == "__main__":
    loading_screen()
    
    '''
    while True:
        search_query = search_screen()
        result_file = searchhandling.parse_query(search_query)
        result_screen(search_query, result_file)'''
    