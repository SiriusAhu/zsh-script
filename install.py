# 将以上脚本改为python版本

import os
import sys
import shutil
import subprocess
import time

# ---Preparation---
themes = {}
plugins = {}

# themes
themes["powerlevel10k"]="git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"

# plugins
plugins["zsh-syntax-highlighting"]="git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
plugins["zsh-autosuggestions"]="git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
plugins["zsh-history-substring-search"]=" git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search"
plugins["auto-notify"]="git clone https://github.com/MichaelAquilina/zsh-auto-notify.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/auto-notify"
plugins["you-should-use"]="git clone https://github.com/MichaelAquilina/zsh-you-should-use.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/you-should-use"

# ---Main page---
# 第一个界面：列出所有要安装的theme和plugin
print("------------Installation List------------")
print("The following THEMES will be installed:")
for theme in themes:
    print("\t" + theme)

print()
print("The following PLUGINS will be installed:")
for plugin in plugins:
    print("\t" + plugin)

# 第二个界面：显示安装过程

# 第三个界面：提示哪些成功安装，哪些失败，提示在失败时使用手动安装或者使用代理，提示.zshrc已被修改