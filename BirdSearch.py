''' HATCHING TWITTER AP LANGUAGE FINAL PROJECT '''

import keyboard, time

# Clearing terminal
import os, platform
def CLEAR_TERMINAL():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
# Window Sizing Handling
'''def window_size():
    size = os.get_terminal_size()
    
    while True'''

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
#special_characters = compile("[@_!#$%^&*()<>?/\|}{~:]")

def loading_screen():
    CLEAR_TERMINAL()
    print(platform.system(), platform.version(), platform.architecture(), "\nPython", platform.python_version(), platform.python_implementation(), platform.python_compiler())
    time.sleep(2)
    CLEAR_TERMINAL()

def search_screen():
    CLEAR_TERMINAL()
    print("")
    for l in twitter_ASCII_logo:
        print(l)
    while True:
        # Get user search input
        search_query_preparsed = input("\nSearch: ")
        query_valid = True

        # Search Checking
        for x in search_query_preparsed:    # Checking if any digits in the string
            if x.isdigit():
                query_valid = False
                break
        if search_query_preparsed[0] == "#" and search_query_preparsed.index() < 0:
            return search_query_preparsed

        if query_valid:
            return search_query_preparsed
        else:
            print ("Enter a valid search")

def result_screen(user_search):
    CLEAR_TERMINAL()
    print("Showing results for:", user_search)
    for x in range(0, 20):
        print("-", end="")


# EXECUTE MAIN
if __name__ == "__main__":
    #printLoadingScreen()
    '''
    while True:
        search_query = search_screen()
        print(search_query)
        result_screen(search_query)'''
    search_query = search_screen()
    result_screen(search_query)