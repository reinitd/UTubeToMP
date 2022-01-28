
# Yes, I used a code beautifier...

import os as o

try:
    import colorama

    print("module 'colorama' is installed")
except ModuleNotFoundError:
    print("module 'colorama' is not installed")
    o.system("pip install colorama")
try:
    import pytube

    print("module 'pytube' is installed")
except ModuleNotFoundError:
    print("module 'pytube' is not installed")
    o.system("pip install pytube")
try:
    import moviepy

    print("module 'moviepy' is installed")
except ModuleNotFoundError:
    print("module 'moviepy' is not installed")
    o.system("pip install moviepy")


import time as t
import platform as p
from pytube import YouTube
from moviepy.editor import *
from colorama import init, Fore, Back, Style

rOS = p.system()
if rOS in ("Windows", "NT"):
    init()
else:
    pass


def osClear():
    rOS = p.system()
    if rOS in ("Windows", "NT"):
        o.system("cls")
    else:
        o.system("clear")


def main():
    osClear()
    intro = open("intro.txt", "r")
    print(intro.read())
    link = input(f"{Back.BLACK}Paste the youtube link:{Style.RESET_ALL}\n> ")
    osClear()

    yt = YouTube(link)
    osClear()
    intro = open("intro.txt", "r")
    pretitleVerify = input(
        f"{intro.read()}\n{Back.BLACK}Is this the YouTube video's title? (y/n){Style.RESET_ALL}\n{yt.title}\n> "
    )

    titleVerify = pretitleVerify.lower()
    if titleVerify == "y":
        pass
    elif titleVerify == "n":
        osClear()
        main()
    elif titleVerify == "yes":
        pass
    elif titleVerify == "no":
        osClear()
        main()
    else:
        osClear()
        intro = open("intro.txt", "r")
        print(
            f"{intro.read()}{Back.RED}Duh oh!.. Invalid response, restarting!..{Style.RESET_ALL}"
        )
        t.sleep(2)
        osClear()
        main()

    osClear()
    intro = open("intro.txt", "r")
    print(intro.read())
    prempChoice = input(
        f"{Back.BLACK}Would you like to download as MP4 (Video) or MP3 (Audio)?{Style.RESET_ALL}\n> "
    )

    mpChoice = prempChoice.lower()

    if mpChoice == "mp4":
        try:
            yt = (
                yt.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            yt.download("./")
        except:
            print(
                f"A{Back.RED}n error has occured!... Maybe a connection timeout or the YouTube link is invalid!..{Style.RESET_ALL}"
            )
            t.sleep(2)
            osClear()
            main()

        print(f"{Back.GREEN}Done! Saved into the current directory!..{Style.RESET_ALL}")
        exit()

    elif mpChoice == "mp3":
        try:
            yt = (
                yt.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            yt.download("./")
            print(f"{Back.BLUE}Downloading the mp4...{Style.RESET_ALL}")
            t.sleep(3)
            print(
                f"{Back.BLUE}Converting to mp3, this will take some time depending on the file size!..{Style.RESET_ALL}"
            )
            video = VideoFileClip(f"{yt.title}.mp4")
            video.audio.write_audiofile(f"{yt.title}.mp3")
            if o.path.exists(f"{yt.title}.mp4"):
                o.remove(f"{yt.title}.mp4")
            else:
                pass

        except:
            print(
                f"{Back.RED}An error has occured!... Maybe a connection timeout or the YouTube link is invalid!..{Style.RESET_ALL}"
            )
            t.sleep(2)
            osClear()
            main()

        print(f"{Back.GREEN}Done! Saved into the current directory!..{Style.RESET_ALL}")
        exit()

    elif mpChoice == "video":
        try:
            yt = (
                yt.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            yt.download("./")
        except:
            print(
                f"{Back.RED}An error has occured!... Maybe a connection timeout or the YouTube link is invalid!..{Style.RESET_ALL}"
            )
            t.sleep(2)
            osClear()
            main()

        print(f"{Back.GREEN}Done! Saved into the current directory!..{Style.RESET_ALL}")
        exit()

    elif mpChoice == "audio":
        try:
            yt = (
                yt.streams.filter(progressive=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
                .first()
            )
            yt.download("./")
            print(f"{Back.BLUE}Downloading the mp4...{Style.RESET_ALL}")
            t.sleep(3)
            print(
                f"{Back.BLUE}Converting to mp3, this will take some time depending on the file size!..{Style.RESET_ALL}"
            )
            video = VideoFileClip(f"{yt.title}.mp4")
            video.audio.write_audiofile(f"{yt.title}.mp3")
            if o.path.exists(f"{yt.title}.mp4"):
                o.remove(f"{yt.title}.mp4")
            else:
                pass

        except:
            print(
                f"{Back.RED}An error has occured!... Maybe a connection timeout or the YouTube link is invalid!..{Style.RESET_ALL}"
            )
            t.sleep(2)
            osClear()
            main()

        print(f"{Back.GREEN}Done! Saved into the current directory!..{Style.RESET_ALL}")
        exit()

    else:
        osClear()
        print(f"{Back.RED}Duh oh!.. Invalid response, restarting!..{Style.RESET_ALL}")
        t.sleep(2)
        osClear()
        main()


if __name__ == "__main__":
    main()

#############################
# GitHub => russian-dev     #
# Instagram => russian.devv #
#############################
