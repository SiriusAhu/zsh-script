import os

FILE_PATH = os.path.expanduser("~/.zshrc")

# region Simple Parameters

# ---Preparation---
THEMES = {}
NEW_PLUGINS = {}
fonts = {}

# themes
THEMES[
    "powerlevel10k"
] = "git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"

# plugins
NEW_PLUGINS[
    "zsh-syntax-highlighting"
] = "git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
NEW_PLUGINS[
    "zsh-autosuggestions"
] = "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
NEW_PLUGINS[
    "zsh-history-substring-search"
] = " git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search"
NEW_PLUGINS[
    "auto-notify"
] = "git clone https://github.com/MichaelAquilina/zsh-auto-notify.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/auto-notify"
NEW_PLUGINS[
    "you-should-use"
] = "git clone https://github.com/MichaelAquilina/zsh-you-should-use.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/you-should-use"

# fonts
"""
MesloLGS NF Regular.ttf
MesloLGS NF Bold.ttf
MesloLGS NF Italic.ttf
MesloLGS NF Bold Italic.ttf
"""
fonts[
    "MesloLGS NF Regular.ttf"
] = "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf"
fonts[
    "MesloLGS NF Bold.ttf"
] = "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf"
fonts[
    "MesloLGS NF Italic.ttf"
] = "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf"
fonts[
    "MesloLGS NF Bold Italic.ttf"
] = "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf"

# endregion


# region Simple Functions
def UserMakesure(ipt):
    "Ask user to make sure to continue the installation"
    if ipt not in ["", "Y", "y"]:
        if ipt not in ["n", "N"]:
            print("Invalid input!")
        else:
            return False
    return True


def UserContinue():
    print()
    # Press any key to continue
    print("- Press any key to continue...")
    input()


def _locate_plugins(content):
    """Return all the exsisting plugins"""
    start_index = -1
    end_index = -1
    for index in range(len(content)):
        if "(" in content[index]:
            start_index = index
        if ")" in content[index]:
            end_index = index
            break
    content_index = end_index - start_index
    assert content_index >= 0, "WRONG FORMAT!!! Please check your ~/.zsh file!"

    # search from start_index to end_index, record all the plugins:
    """
    Considering these 2 styles:
    plugins=(
    git
	test01
	test02	
    )

    plugins=(git test01	test02)
    """
    plugins = []
    temp = []
    for index in range(start_index, end_index + 1):
        if "(" in content[index]:
            temp.append(content[index].split("(")[1].strip())
        elif ")" in content[index]:
            temp.append(content[index].split(")")[0].strip())
        else:
            temp.append(content[index].strip())
    for item in temp:
        if item:
            plugins.extend(item.split(" "))
    # TODO: Simplify this:
    # check the lask plugin in plugins, if it contains a ")", if so remove it
    if ")" in plugins[-1]:
        plugins[-1] = plugins[-1].split(")")[0]
    return plugins


def _write_in(content):
    with open(FILE_PATH, "w") as f:
        f.writelines(content)


# endregion


# region Page Functions
def _page1():
    print("The following THEMES will be installed:")

    for theme in THEMES:
        print("\t" + theme)

    print()
    print("The following PLUGINS will be installed:")
    for plugin in NEW_PLUGINS:
        print("\t" + plugin)

    print()
    print("- Are you sure to install them? (Y/n)")
    UserMakesure(input())


def _page3():
    # ---Install themes---
    print("Installing themes...")
    print()
    for theme in THEMES:
        print("Installing " + theme + "...")
        os.system(THEMES[theme])
        print()
    print("Done!")

    # ---Install plugins---
    print("Installing plugins...")
    print()
    for plugin in NEW_PLUGINS:
        print("Installing " + plugin + "...")
        os.system(NEW_PLUGINS[plugin])
        print()
    print("Done!")


def _page4():
    # ---Edit .zshrc---
    print("Editing .zshrc...")
    print()

    # ---Add themes---
    # Try to find the line of ZSH_THEME, and replace it with ZSH_THEME="powerlevel10k/powerlevel10k"
    # If not found, assert and exit
    try:
        # Find the line of ZSH_THEME
        for i in range(len(lines)):
            if lines[i].startswith("ZSH_THEME"):
                lines[i] = 'ZSH_THEME="powerlevel10k/powerlevel10k"\n'
                break
        else:
            raise Exception(
                "Heeeeeeeeeeeeeeey!ZSH_THEME not found! Please make sure you have installed oh-my-zsh!"
            )
        # Write the new .zshrc
        _write_in(lines)
    except Exception as e:
        print(e)
        print("Installation aborted.")
        exit(1)

    print("ZSH_THEME added.")

    # ---Add plugins---
    # Try to find the line of plugins, and add plugins to it
    try:
        # Find the line of plugins(Already found at the beginning)
        # Edit the plugins lines (We store it in many-lines style)
        """
        plugins=(
            git
            xxx01
            xxx02
        )
        """
        plugin_lines = []
        # remain the exsisting plugins
        for plugin in exsisting_plugins:
            plugin_lines.append("    " + plugin + "\n")
        for plugin in NEW_PLUGINS:
            plugin_lines.append("    " + plugin + "\n")
        # Add plugins to the line of plugins
        for i in range(len(lines)):
            # Replace the lines between '(' and ')' with plugin_lines
            if "(" in lines[i]:
                start_index = i
            if ")" in lines[i]:
                end_index = i
                break
        if start_index == end_index:
            # rewrite the first line, and add the ')' after the last line
            lines[start_index] = "plugins=(\n"
            plugin_lines.append(")\n")
        lines[start_index + 1 : end_index] = plugin_lines
        # Write the new .zshrc
        _write_in(lines)
    except Exception as e:
        print(e)
        print("Installation aborted.")
        exit(1)

    print("Plugins added.")


def _page5():
    # ---Download fonts---
    # Download 4 fonts into ~/Downloads using 'curl'
    print("Downloading fonts...")
    print()
    for font in fonts:
        print("Downloading " + font + "...")
        # Download with wget
        download_command = "wget " + fonts[font] + " -P ~/Downloads"
        os.system(download_command)
        print()

    print("Done!")


# endregion

# region 0 Preparation

# Get the content of ~/.zshrc
with open(FILE_PATH, "r") as f:
    lines = f.readlines()

exsisting_plugins = _locate_plugins(lines)

# Compare the exsisting plugins with the plugins to be installed, and remove the same ones
plugins_to_remove = []

for plugin in NEW_PLUGINS:
    if plugin in exsisting_plugins:
        plugins_to_remove.append(plugin)

for plugin in plugins_to_remove:
    NEW_PLUGINS.pop(plugin)


# endregion

# --------------------------------Main pages--------------------------------
# region - Page 1: List all themes and plugins to be installed
os.system("clear")
print("------------Installation List------------")
_page1()
# endregion

# region - Page 2: Install themes and plugins(Record which ones are successfully installed)
os.system("clear")
print("------------Installing------------")

_page3()

UserContinue()
# endregion

# region - Page 3: Edit .zshrc
os.system("clear")
print("------------Editing .zshrc------------")
# Ask if user want the script to edit .zshrc
print(
    "- Do you want the script to edit .zshrc for you? \
      \nIt will remain the plugins you have installed.(Y/n)"
)
if UserMakesure(input()):
    _page4()
else:
    print("\n- OK.")

UserContinue()
# endregion

# region - Page 4: Download fonts
os.system("clear")
print("------------Download fonts------------")
# Ask if user want the script to install fonts
print("- Do you want the script to download fonts for you?")
print("Here shows the fonts that powerlevel10k needs:")
print("https://github.com/romkatv/powerlevel10k/blob/master/font.md")
print()
print("If so, the script will download the 4 font files for you.")
print("They will be download into your Downloads folder.(Y/n)")
if UserMakesure(input()):
    _page5()
else:
    print("\n- OK.")
UserContinue()
# endregion

# region - Page 5: After installation
os.system("clear")
print("------------After Installation------------")
print("Here is the end of the installation script.")
print("You may do the following things manually:(Optional)")
print("    1. You can open your ~/Downloads folder and install the fonts.")
print(
    "    2. You can check your ~/.zshrc file and make sure the plugins( and theme) are added."
)
print()
print("- Your ~/.zshrc file should be in this format:")
print(
    'For the theme:\
    \n    ZSH_THEME="powerlevel10k/powerlevel10k"'
)
print()
print(
    "For the plugins:\
    \n(xxx01 and xxx02 are the plugins you want to install)\
    \n    plugins=(\
    \n        git\
    \n        xxx01\
    \n        xxx02\
    \n        ...\
    \n    )"
)
print("\n At last, you can restart your terminal and enjoy your new zsh!")
# endregion
