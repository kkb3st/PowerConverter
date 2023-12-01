#!/usr/bin/python

# -------------------- IMPORTS -------------------- #
from files.converters import *
from colorama import Fore, Style  # , Back
import sys
import argparse


# -------------------- BANNERS -------------------- #
banner_console = Fore.GREEN + r"""                                                         
 _____                        _____                          _             
|  __ \                      / ____|                        | |            
| |__) |____      _____ _ __| |     ___  _ ____   _____ _ __| |_ ___ _ __  
|  ___/ _ \ \ /\ / / _ \ '__| |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| 
| |  | (_) \ V  V /  __/ |  | |___| (_) | | | \ V /  __/ |  | ||  __/ |    
|_|   \___/ \_/\_/ \___|_|   \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    

V.1.6.4                                 created by kk, github.com/kk-dev7
""" + Style.RESET_ALL

banner_converters = """
Supported File Types:

Image:      .png     .jpg     .ico     .webp
Video:      .mp4     .avi     .mov     .flv
Audio:      .mp3     .wav   
"""

banner_usage = Fore.BLUE + "\nInput Format: to-[DesiredOutputFormat]  ---> example: to-mp4\n" + Style.RESET_ALL

# -------------------- VARIABLES -------------------- #

converters = {
    # Image
    "to-jpg": anything_to_jpg, "to-ico": anything_to_ico, "to-webp": anything_to_webp, "to-png": anything_to_png,

    # Video
    "to-mov": anything_to_mov, "to-mp4": anything_to_mp4, "to-avi": anything_to_avi, "to-flv": anything_to_flv,

    # Audio
    "wav-mp3": wav_to_mp3, "mp3-wav": mp3_to_wav,
}


# -------------------- FUNCTIONS -------------------- #
def convert(c):
    if c in converters:
        f = input("\n[-] Please provide the path of the file you want to convert: ")
        f = [f.strip() for f in f.split(';')]
        converters[c](f)
    else:
        print(Fore.RED + "[ERROR] Please provide a valid converter!" + Style.RESET_ALL)


def advanced_convert(c, f):  # c = converter, f = files
    if not f:
        print(Fore.RED + "[ERROR] Please provide either a single file or a list of files." + Style.RESET_ALL)
        return

    # if the user provided a single file, make a list out of it
    if not isinstance(f, list):
        f = [f]

    # check the given converter and if valid, convert the file
    if c in converters:
        converters[c](f)
    else:
        print(Fore.RED + "[ERROR] Please provide a valid converter!" + Style.RESET_ALL)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    user_continue = "y"
    # DEFAULT / USER-FRIENDLY MODE
    if not len(sys.argv) > 1:
        while user_continue.lower() == "y":  # While the user wants to continue converting...
            print(banner_console + banner_converters + banner_usage)
            print("[-] Please enter a converter you want to use:")
            convert(input(">"))
            print("\n[-] Do you want to continue converting? (y/n)")
            user_continue = input(">")
            clear_screen()

    # ADVANCED MODE
    else:
        print(banner_console)
        # argumentList = sys.argv[1:]

        parser = argparse.ArgumentParser(description=None)

        parser.add_argument("-f", "--file", help="Choose a file to convert")
        parser.add_argument("-c", "--converter", help="Choose a conversion method")
        parser.add_argument("-l", "--list", help="Choose a list of files to convert (semicolon-separated)")

        args = parser.parse_args()

        if args.file and args.list:
            print(Fore.RED + "[ERROR] Please provide either a single file or a list of files, not both." +
                  Style.RESET_ALL)

        if args.file:
            # if a single file is given, pass it to convert function
            advanced_convert(args.converter, args.file)
        elif args.list:
            # if the argument file list is given, pass the list to convert function
            advanced_convert(args.converter, [f.strip() for f in args.list.split(';')])
        else:
            print(Fore.RED + "[ERROR] Please specify a file or a list of files to convert!")


if __name__ == "__main__":
    main()
