import os
from utils.utils import *

def _exit():
    print("  Bye!")
    exit(0)

def tip_userMakeDecision(inpt):
    """
    Enter, Y, y -> True
    N, n -> False
    else -> Invalid input!
    """
    if inpt not in ["", "Y", "y"]:
        if inpt not in ["n", "N"]:
            text_ = "Invalid input!"
            raise ValueError(text_ + "\n" + TEXT_DONT_WORRY)
        else:
            return False
    return True

def tip_userContinue(text="- Press any key to continue..."):
    # Press any key to continue
    print(text)
    input()



def page0(plugins, theme):
    print("---- Welcome ---")
    print("  This is a script to help you install some useful theme and plugins for zsh:")
    print("  Please make sure you have installed \033[41mzsh\033[0m and \033[41moh-my-zsh\033[0m before. (alos, \033[41mwget\033[0m is needed for download fonts)")
    print("Plugins:")
    for plugin in plugins:
        print("\t" + plugin)
    print("Theme:")
    print("\t" + theme)
    print()
    print("# Note: About backup #")
    print("  Don't worry, this script will automatically do 2 backups for you:")
    print(f"\t1. At first run, it will backup your {HOME}/.zshrc file to {ORIGIN_PATH}.")
    print("\t- This file will be used when you want to reset your .zshrc file. (It won't be change after created)")
    print(f"\t2. At every run, it will backup your {HOME}/.zshrc file to {ZSHRC_BAK}.")
    print("\t- This file will be **overwritten** at every run.")
    print()
    print("- Do you want to continue? (Y/n)")
    inpt = input()
    if not tip_userMakeDecision(inpt):
        _exit()
    os.system("clear")

def page1(plugins_addition):
    print("---- Before installation ----")
    print("  Here are some integrated plugins which are of good use:")
    for plugin in plugins_addition:
        print("\t" + plugin)
    print("- Do you want to install them? (Y/n)")
    inpt = input()
    addition = tip_userMakeDecision(inpt)
    os.system("clear")
    return addition

def page2(plugins, theme, plugins_links, theme_link, plugins_bool, theme_text, plugins_addtion):
    print("---- Installation ----")
    print("  This method will install the following plugins:")
    for plugin in plugins:
        print("\t" + plugin)
    for plugin in plugins_addtion:
        print("\t" + plugin)
    print("  This method will install the following theme:")
    print("\t" + theme)
    print("- Are you sure to download them? (Y/n)")
    inpt = input()
    if not tip_userMakeDecision(inpt):
        _exit()
    print()

    print("# Note: Installing... #")
    print()
    for link in plugins_links:
        # For "zsh-you-should-be", it should be put at "$ZSH_CUSTOM/plugins/you-should-use"
        if link.split("/")[-1] == "zsh-you-should-use":
            gclone("${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins", link)
        else:
            gclone("${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins", link)
    gclone("${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes", theme_link)
    
    print("# Note: Installation completed #")
    tip_userContinue()
    os.system("clear")
    
    print("---- Installation ----")
    print("- Do you want to this script to edit your .zshrc file? (Y/n)")
    print("# Note: Your original and current .zshrc file have been backed up #")
    inpt = input()
    if tip_userMakeDecision(inpt):
        print("# Note: Editing... #")
        edit_zshrc(ZSHRC_HOME, plugins, plugins_bool, plugins_addtion, theme_text)
        print("# Note: Editing completed #")
    print("# Note: Installation completed #")

    tip_userContinue()
    os.system("clear")

def page3(fonts, fonts_links):
    print("---- Font Download ----")
    print("  This method will download the following fonts, which required by powerlevel10k:")
    for font in fonts:
        print("\t" + font)
    print("  These fonts will be downloaded into your ~/Downloads folder.")
    print("- Are you sure to download them? (Y/n)")
    inpt = input()
    if tip_userMakeDecision(inpt):
        print()
        for link in fonts_links:
            download(f"{HOME}/Downloads", [link])
        print("# Note: Download completed #")
        print("# Note: You should install the fonts manually #")

    tip_userContinue()
    os.system("clear")

def page4():
    print("---- After Installation ----")
    print("  Here is the end of the installation script.")
    print("  Thanks for using this script!")
    print("# Note: You can \033[44mreset\033[0m your .zshrc file to its original state by running:")
    print("\tpython reset.py")
    