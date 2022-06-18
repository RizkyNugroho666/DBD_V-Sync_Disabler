import os                                                                           # Coded by: 1ntrovertskrrt
import time
import shutil
import stat
import webbrowser
import colorama
from stat import S_IREAD, S_IRGRP, S_IROTH
from pathlib import Path
from colorama import Fore

home = str(Path.home())
colorama.init()

gamePlatfrom = ["WindowsNoEditor", "EGS", "WinGDK"] # [Steam] [Epic Games] [Microsoft Store] | Array

def menu(): # Menu
    ascii()
    print("Select What You Want!?")
    print("\n[1] Disable V-Sync Steam\n[2] Disable V-Sync Epic Games\n[3] Disable V-Sync Microsoft Store\n[4] Fix Config Error(Restore to default settings)\n[5] Join Discord\n[6] Exit")

def disableVsync(): # MAIN PROGRAM!!!

    # Null String Variable
    command = ""
    selectedGamePlatfrom = ""

    while True:
        menu()
        try:
            command = str(input("\n>> ")) # Input Command

            if command == "1":
                selectedGamePlatfrom = gamePlatfrom[0]
            
            elif command == "2":
                selectedGamePlatfrom = gamePlatfrom[1]
            
            elif command == "3":
                selectedGamePlatfrom = gamePlatfrom[2]
            
            elif command == "4":
                os.system('cls')
                fixerror()
                return disableVsync()

            elif command == "5":
                os.system('cls')
                openDiscord()
                return disableVsync()

            elif command == "6":
                os.system('exit')
                break

            else:
                print(Fore.RED+"\nInvalid Command! Please enter a number!"+Fore.WHITE)
                time.sleep(2)
                os.system('cls')
                return disableVsync()

        except FileExistsError:
            print(Fore.RED+"\nAn Unknown Error Occured!"+Fore.WHITE)
            time.sleep(2)
            os.system('cls')
            return disableVsync()

        try:
            print(Fore.GREEN+"\nDisabling your V-Sync..."+Fore.WHITE)
            time.sleep(2)

            # Check if Read Only, then set to not Read Only
            GameUserSettings = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini" # Config File
            os.chmod(GameUserSettings, stat.S_IWRITE)

            Engine = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini" # Engine File
            os.chmod(Engine, stat.S_IWRITE)

            # Remove Current Engine file and replace it with default Engine file & Copy the original to Config Location
            Engine = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini" # Engine File
            os.remove(Engine)

            Engine_src = "Resources\\Backup\\Engine.ini"
            Engine_dst = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\"
            shutil.copy(Engine_src, Engine_dst)

            try:
                GameUserSettings_Res = "Resources\\GameUserSettings.ini" # Config File
                os.chmod(GameUserSettings_Res, stat.S_IWRITE)

                Engine_Res = "Resources\\Engine.ini" # Engine File
                os.chmod(Engine_Res, stat.S_IWRITE)

            except FileNotFoundError:
                pass

            # GameUserSettings.ini (Copy from Current Location)
            config_dst = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini" # Config File
            config_target = "Resources"

            shutil.copy(config_dst, config_target) # Copy the original Config to Resources folder, to edit and re-copy it again to dbd config file location

            # Engine.ini (Copy from Current Location)
            engine_dst = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini" # Engine File
            engine_target = "Resources"

            shutil.copy(engine_dst, engine_target) # Copy the original Engine to Resources folder, to edit and re-copy it again to dbd config file location

            # Change Config (MOST IMPORTANT CODE!!!)
            with open("Resources\\GameUserSettings.ini", "rt") as config_res, open(f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini", "wt") as config_dbd:
                for line in config_res:
                    config_dbd.write(line.replace('bUseVSync=True','bUseVSync=False'))
            
            with open(f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini", "a") as engine_dbd:
                engine_dbd.write('\n[/script/engine.engine]\nbSmoothFrameRate=false')

            # Make The Engine FIle Read Only
            Engine = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini" # Engine File
            os.chmod(Engine, S_IREAD|S_IRGRP|S_IROTH) # Lock Engine.ini, prevent the dbd restore this file to default

            # Finished
            print(Fore.GREEN+"\nV-Sync Disabled!"+Fore.WHITE)
            time.sleep(2)
            os.system('cls')
            return disableVsync()

        except FileNotFoundError:
            print(Fore.RED+"\nConfig File Not Found!"+Fore.WHITE)
            time.sleep(2)
            os.system('cls')
            continue

    return

def openDiscord(): # Open my discord server to default browser
    url = "https://discord.gg/nb3c2bxcfg"
    webbrowser.open(url)

def fixerror(): # Fix Config Error & Restore it to default
    ascii()
    print("Select your Game Platfrom!")
    print("\n[1] Restore DBD Steam Config\n[2] Restore DBD Epic Games Config\n[3] Restore DBD Microsoft Config")
    command = str(input(Fore.GREEN+"\n>> "+Fore.WHITE)) # Input Command
    if command == "1":
        selectedGamePlatfrom = gamePlatfrom[0]
    
    elif command == "2":
        selectedGamePlatfrom = gamePlatfrom[1]
    
    elif command == "3":
        selectedGamePlatfrom = gamePlatfrom[2]

    print("\nRestoring your config files...")
    time.sleep(2)
    try:
        # Remove Read Only to remove the files
        GameUserSettings = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini" # Config File
        os.chmod(GameUserSettings, stat.S_IWRITE)

        Engine = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini" # Engine File
        os.chmod(Engine, stat.S_IWRITE)

        # Remove Current Config
        GameUserSettings = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini" # Config File
        os.remove(GameUserSettings)

        # Remove Current Engine
        Engine = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini" # Engine File
        os.remove(Engine)

    except FileNotFoundError:
        pass

    try:
        # Copy Backup Config to DBD Config Location
        GameUserSettings_Backup = "Resources\\Backup\\GameUserSettings.ini"
        GameUserSettings_Dst = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\GameUserSettings.ini"
        shutil.copy(GameUserSettings_Backup, GameUserSettings_Dst)

        # Copy Backup Engine to DBD Config Location
        Engine_Backup = "Resources\\Backup\\Engine.ini"
        Engine_Dst = f"{home}\\AppData\\Local\\DeadbyDaylight\\Saved\\Config\\{selectedGamePlatfrom}\\Engine.ini"
        shutil.copy(Engine_Backup, Engine_Dst)

        print(Fore.GREEN+"\nConfig has been restored to default settings!"+Fore.WHITE)
        time.sleep(2)
        os.system('cls')

    except FileNotFoundError:
        print("\nConfig Not Found! Please select valid platfrom!")
        os.system('cls')
        time.sleep(2)
        pass

def ascii():
    print("""
██    ██       ███████ ██    ██ ███    ██  ██████     ██████  ██ ███████  █████  ██████  ██      ███████ ██████  
██    ██       ██       ██  ██  ████   ██ ██          ██   ██ ██ ██      ██   ██ ██   ██ ██      ██      ██   ██ 
██    ██ █████ ███████   ████   ██ ██  ██ ██          ██   ██ ██ ███████ ███████ ██████  ██      █████   ██████  
 ██  ██             ██    ██    ██  ██ ██ ██          ██   ██ ██      ██ ██   ██ ██   ██ ██      ██      ██   ██ 
  ████         ███████    ██    ██   ████  ██████     ██████  ██ ███████ ██   ██ ██████  ███████ ███████ ██   ██ 
                                                                                                                 

                                               Dead by Daylight
                                            
                                            Author = 1ntrovertskrrt
                                         Boost your FPS more than 60!!!

                                                                                                                 """)

if __name__ == '__main__':
    disableVsync()
