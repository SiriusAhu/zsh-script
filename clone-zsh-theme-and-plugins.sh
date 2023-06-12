#!/bin/bash

# 注意事项：
# 1. 请使用bash运行此脚本
# 2. 请不要使用sudo运行此脚本
# 3. 请确保所有的git命令的目标文件夹都是正确的形式（见下方的注释）

echo -e "Please \e[41muse \e[33mbash\e[0m to run this script!\e[0m"
echo -e "Please \e[41mdon't use \e[33msudo\e[0m to run this script!\e[0m"

# 将所有theme，plugin与其对应的command写成关联数组
declare -A themes

# ---Theme list
# powerlevel10k


themes["powerlevel10k"]="git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
theme_directory="powerlevel10k/powerlevel10k"

# themes["test01"]="echo \"git clone test01\""
# theme_directory="test01/test01"

# ---Plugin list
# zsh-syntax-highlighting
# zsh-autosuggestions
# zsh-history-substring-search
# auto-notify
# you-should-use

# ------------------------注意这里：有一些git的命令的目标文件夹需要修改------------------------
# 观察下方，zsh-history-substring-search的目标文件夹是${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search"
# 而auto-notify的目标文件夹是$ZSH_CUSTOM/plugins/auto-notify
# $ZSH_CUSTOM/plugins/auto-notify"
#
# 我们需要改为前者的形式
# ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/auto-notify"

declare -A plugins


plugins["zsh-syntax-highlighting"]="git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting"
plugins["zsh-autosuggestions"]="git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions"
plugins["zsh-history-substring-search"]=" git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search"
plugins["auto-notify"]="git clone https://github.com/MichaelAquilina/zsh-auto-notify.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/auto-notify"
plugins["you-should-use"]="git clone https://github.com/MichaelAquilina/zsh-you-should-use.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/you-should-use"

# Plugins["test01"]="echo \"git clone test01\""
# Plugins["test02"]="echo \"git clone test02\""
# Plugins["test03"]="echo \"git clone test03\""

# automatically put all pugins into a variable
all_plugins=""
for plugin in "${!plugins[@]}"; do
    all_plugins="$all_plugins $plugin"
done

# ---Main script

echo "- This script will clone the zsh theme and plugins from github."
echo "- To install them, you need to modify the .zshrc file!"
echo ""

# Show the list of themes and plugins
# Themes
echo -e "\033[34mHere is the list of themes and plugins:\033[0m"

echo -e "\033[33m\033[1m--------Themes--------\033[0m"
for theme in "${!themes[@]}"; do
    echo -e "\033[33m - $theme\033[0m"
done
echo ""
# Plugins
echo -e "\033[33m\033[1m--------Plugins--------\033[0m"
for plugin in "${!plugins[@]}"; do
    echo -e "\033[33m - $plugin\033[0m"
done
echo ""


# Ask for confirmation
read -p "Do you want to continue? [Y/n] " answer
if [[ $answer == "Y" || -z $answer ]]; then

    clear

    # Theme main
    echo -e "\033[1m--------Cloning started--------\033[0m"
    echo ""

    echo -e "\033[33m\033[1m--------Cloning zsh themes--------\033[0m"
    echo ""
    
    for key in "${!themes[@]}"; do
        echo -e "\033[33m\033[1m - Cloning theme -- $key...\033[0m"
        eval "${themes[$key]}"
        echo ""
    done
    

    echo -e "\033[33m\033[1m - All the themes are cloned.\033[0m"
    echo ""



    # Plugins main
    echo -e "\033[33m\033[1m--------Cloning zsh plugins--------\033[0m"
    echo ""

    for key in "${!plugins[@]}"; do
        # echo "hi"
        echo -e "\033[33m\033[1m - Cloning plugin -- $key...\033[0m"
        eval "${plugins[$key]}"
        echo ""
    done


    echo -e "\033[33m\033[1m - All the plugins are cloned.\033[0m"
    


    echo ""
    echo ""
    echo "Press any key to continue..."
    read -n 1

    clear
    
    
    echo -e "\033[1m\e[41mPlease manually modify the \033[0m\e[41m\033[33m\033[1m.zshrc\033[0m\e[41m\033[1m file to install the theme and plugins.\033[0m"
    echo ""
    echo -e "\033[1mAdd the following lines to the \033[0m\033[33mplugins\033[0m\033[1m section:\033[0m"
    for plugin in $all_plugins; do
        echo -e "\033[36m    $plugin\033[0m"
    done
    echo ""

    # Example:
    # plugins=(
    #     # ...
    #     xxx1
    #     xxx2
    #     xxx3
    #     # ...
    # )
    echo -e "\033[1mFor example:\033[0m"
    echo -e "\033[36mplugins=(\033[0m"
    echo -e "\033[36m    # ...\033[0m"
    echo -e "\033[36m    xxx1\033[0m"
    echo -e "\033[36m    xxx2\033[0m"
    echo -e "\033[36m    xxx3\033[0m"
    echo -e "\033[36m    # ...\033[0m"
    echo -e "\033[36m)\033[0m"


    echo -e "\033[1mChange the \033[0m\033[33m\033[1mZSH_THEME\033[0m\033[1m to this:\033[0m"
    # 显示theme_directory
    echo -e "\033[33mZSH_THEME=\"$theme_directory\"\033[0m"

else
    echo -e "\033[33mAborting...\033[0m"
fi




# while true; do
#     read -p "Please enter Y or N: " yn
#     case $yn in
#         [Yy]* )
#             echo "helo"
#             break;;
#         [Nn]* )
#             exit;;
#         * )
#             echo "illegal input";;
#     esac
# done
