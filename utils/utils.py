import os

TEXT_DONT_WORRY = "Don't worry, the files will only be edited at the end of the process."

HOME = os.environ["HOME"]
# ZSHRC_HOME = "fake_home/.zshrc" # TODO: change it 
ZSHRC_HOME = os.path.join(HOME, ".zshrc")
ZSHRC_BAK = "./bak/.zshrc.bak"

ZSHRC_DEFAULT = "bak/.zshrc_default"
ORIGIN_DIRECTORY = "./LOOK_AT_ME_YOUR_ZSHRC_IS_BACKUPED_HERE"
ORIGIN_NAME = ".zshrc.origin"
ORIGIN_PATH = f"{ORIGIN_DIRECTORY}/{ORIGIN_NAME}"
ORIGIN_PATH_ABS = os.path.join(os.getcwd(), ORIGIN_PATH.split('/')[1])

def gclone(directory:str, link:str)-> None:
    """Download a file from a given link and save it in a given directory.
    
    Args:
        name (str): Name of the file to be saved.
        directory (str): Directory where the file will be saved.
        link (str): Link to download the file from.
    """    
    # clone the repo in "directory"
    name = link.split("/")[-1].split(".")[0]
    os.system(f"git clone {link} {directory}")

def download(directory, links):
    """
    download files from links and save them in directory (wget)
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # download files
    for link in links:
        os.system(f"wget {link} -P {directory}")

def backup_zshrc():
    """
    soft backup:
    if ~/.zshrc exists, copy it to zsh_back_path
    else copy the default .zshrc to zsh_back_path

    hard backup:
    if ~/.zshrc exists, a origin directory will be created at the first run
    and the original .zshrc will be copied to the origin directory
    This copied file won't be overwritten
    """
    zshrc_exist = os.path.exists(f"{HOME}/.zshrc")
    origin_exist = os.path.exists(f"{ORIGIN_PATH}")
    if zshrc_exist:
        cp = f"cp {HOME}/.zshrc {ZSHRC_BAK}"
        # back up in origin directory
        # will not back up if origin file exists (make sure it's the original file)
        if not origin_exist:
            os.system(f"mkdir -p {ORIGIN_DIRECTORY}")
            os.system(f"cp {HOME}/.zshrc {ORIGIN_PATH}")

            print("# Note: Backup created #")
            print("\tThis directory holds the original .zshrc file (the one before the installation):")
            print(f"\t{ORIGIN_PATH_ABS}")
    else:
        cp = f"cp {ZSHRC_DEFAULT} {ZSHRC_BAK}"
    if origin_exist:
        print("# Note: Backup is ready #")
        print("  Your .zshrc file has been backed up before:")
        print(f"\t{ORIGIN_PATH_ABS}")
        print("  It won't be backed up again.")
        print("  If you want to reset your .zshrc file to its original state, run:")
        print("\tpython reset.py")

    os.system(cp)
    

def edit_zshrc(zshrc_path, plugins, plugins_bool, plugins_addtion, theme_text):
    """
    edit zshrc file
    """
    # edit plugins
    edit_plugins(zshrc_path, plugins, plugins_bool, plugins_addtion)

    # # edit theme (only for powerlevel10k)
    edit_theme_p10k(zshrc_path, theme_text)


#region - edit plugins
def edit_plugins(zshrc_path, plugins, plugins_bool, plugins_addtion):
    old_plugins_info = find_old_plugins(zshrc_path)
    old_plugins = old_plugins_info["old_plugins"]
    start_line = old_plugins_info["start_line"]
    end_line = old_plugins_info["end_line"]

    # find new plugins
    for i, item in enumerate(plugins):
        if item in old_plugins:
            plugins_bool[i] = False
    new_plugins = [item for item, keep in zip(plugins, plugins_bool) if keep]
    # new_plugins: new_plugins + old_plugins + plugins_addtion
    new_plugins.extend(old_plugins)
    if plugins_addtion != []:
        new_plugins.extend(plugins_addtion)
    # sort: from a to z
    new_plugins.sort(reverse=True)

    # write in new plugins
    write_zshrc_plugin(zshrc_path, new_plugins, start_line, end_line)

def find_old_plugins(zshrc_path):
    """
    find all old_plugins in zshrc_path
    style1:
    plugins=(
        git
        zsh-syntax-highlighting
        zsh-autosuggestions
        zsh-history-substring-search
        auto-notify
        you-should-use
        )
    style2:
    plugins=(git zsh-syntax-highlighting zsh-autosuggestions zsh-history-substring-search auto-notify you-should-use)
    """
    old_plugins = []
    start_line = -1
    end_line = -1
    text= None

    with open(zshrc_path, "r") as f:
        lines = f.readlines()
        text = lines
    
    findPluginLine = False
    isStyle2 = False
    for i, line in enumerate(text):
        # line begins with "plugins=("
        if line.strip().startswith("plugins=("):
            findPluginLine = True
            start_line = i
            end_line = i
            # style 1
            if ")" in line:
                old_plugins = line.split("plugins=(")[1].split(")")[0].split(" ")
                for i, item in enumerate(old_plugins):
                    if item == '':
                        old_plugins.pop(i)
                break
            # style 2
            else:
                isStyle2 = True
        if ")" in line and findPluginLine:
            end_line = i
            break
    
    if isStyle2:
        text_ = []
        record = False
        for line in text:
            if line.startswith("plugins=("):
                record = True
            if record:
                text_.append(line)
                if ")" in line:
                    break
        
        for i, line in enumerate(text_):
            plugin = line.strip()
            if i == 0:
                plugin = line.split("(")[1].strip()
            if i == len(text_) - 1:
                plugin = line.split(")")[0].strip()
            if plugin != '':
                old_plugins.append(plugin) 

    info = {
        "old_plugins": old_plugins,
        "start_line": start_line,
        "end_line": end_line,
    }
    return info

def write_zshrc_plugin(zshrc_path, new_plugins, start_line, end_line):
    """
    Remove old plugins and write in new plugins
    style:
    plugins=(
        git
        zsh-syntax-highlighting
        zsh-autosuggestions
        zsh-history-substring-search
        auto-notify
        you-should-use
        )
    """
    text = None
    with open(zshrc_path, "r") as f:
        lines = f.readlines()
        text = lines
    
    # remove old plugins
    if start_line != -1 and end_line != -1:
        text = text[:start_line] + text[end_line+1:]

    # write in new plugins
    text.insert(start_line, "plugins=(\n")
    for plugin in new_plugins:
        text.insert(start_line+1, f"\t{plugin}\n")
    text.insert(start_line+len(new_plugins)+1, ")\n")

    with open(zshrc_path, "w") as f:
        f.writelines(text)
#endregion

#region - edit theme (only for powerlevel10k)        
def edit_theme_p10k(zshrc_path, theme_text):
    """
    edit theme (only for powerlevel10k)
    find the theme line and replace it
    """
    text = None
    with open(zshrc_path, "r") as f:
        lines = f.readlines()
        text = lines
    
    for i, line in enumerate(text):
        if "ZSH_THEME=" in line:
            text[i] = theme_text + "\n"
            break
    
    with open(zshrc_path, "w") as f:
        f.writelines(text)
#endregion
