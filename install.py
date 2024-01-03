import json
import os
from utils.utils import *
from utils.Interaction import *

PATH_NAME2LINK = "./json/name2link.json"
PATH_NAME2DIRECTORY = "./json/name2directory.json"

plugins_addtion = [
    "copyfile",
    "copypath",
    "copybuffer",
    "sudo",
]

backup_zshrc()
tip_userContinue()
os.system("clear")

link_info = json.load(open(PATH_NAME2LINK))
directory_info = json.load(open(PATH_NAME2DIRECTORY))

theme = list(link_info["theme"].keys())[0]
theme_link = list(link_info['theme'].values())[0]
theme_text = 'ZSH_THEME="powerlevel10k/powerlevel10k"'

plugins = list(link_info["plugins"].keys())
plugins_links = list(link_info['plugins'].values())
plugins_bool = [True] * len(plugins)

fonts = list(link_info["fonts"].keys())
fonts_links = list(link_info['fonts'].values())

page0(plugins, theme)
containAddition = page1(plugins_addtion)
if not containAddition:
    plugins_addtion = []
page2(plugins, theme, plugins_links, theme_link, plugins_bool, theme_text, plugins_addtion)
page3(fonts, fonts_links)
page4()