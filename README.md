## What's this

> version: 2.0

This is a little script to install the plugins(/theme) I use(recommended) in my zsh config.

> When I'm working in a new Linux device which just installed zsh and oh-my-zsh.

## What will be downloaded
Theme:
- powerlevel10k

Plugins:
- zsh-syntax-highlighting
- zsh-autosuggestions
- zsh-history-substring-search
- auto-notify
- you-should-use

## Requirements

Since this script is to install plugins(theme) for `oh-my-zsh`, you should make sure you have installed both `zsh` and `oh-my-zsh`.

- Install `zsh`:
    - For Debian-based Linux(Ubuntu, Linux Mint, etc.):
        ```bash
        sudo apt install zsh
        ```
    - For Arch-based Linux:
        ```bash
        sudo pacman -S zsh
        ```

- Install `oh-my-zsh`:
    `curl`:
    ```bash
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```
    or `wget`:
    ```bash
    sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```
---

## Install & Use

1. Clone this repo:
    ```bash
    git clone https://github.com/SiriusAhu/zsh-scripts.git
    ```

2. Go to the directory:
    ```bash
    cd zsh-scripts
    ```

3. Run the script:
    ```bash
    python3 install.py
    ```

4. Install the fonts if you needed.
    - [The Fonts poverlevel10k recommended](https://github.com/romkatv/powerlevel10k/blob/master/font.md)

5. Restart your terminal and enjoy it!

## Reset
This script will backup both your original and current `~/.zshrc` file
- original: The `~/.zshrc` file before you run this script
    - Used by `reset.py` | won't be overwritten after created
- current: The `~/.zshrc` file after you run this script
    - backup to `./bak/.zshrc.bak` | can be overwritten every time you run this script

If you want to reset your `~/.zshrc` file, just run:
```bash
python3 reset.py
```
---

## QA

Q: I have downloaded my fonts, but why it seems not work?
> A: You may make sure you have set the font in your terminal. For example, in `gnome-terminal`, you can set it in `Edit -> Preferences -> Profiles -> Text Appearance -> Custom font`.

## TODO
- [ ] Add arguments to choose the download path of fonts.