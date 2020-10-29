# Learn shell scripting

Wikipedia definition of Shell:
> A shell is a command-line interpreter which exposes access to an operating system's services. In general, operating system shells use either a command-line interface (CLI) or graphical user interface (GUI), depending on a computer's role and particular operation.

All those technical words are complicated aren't they?
In my opinion, the shortest explanation is this one:  
- Shell == terminal
Wait, what? What is the terminal? The terminal is a way to put commands into your computer mainly done by typing (words, commands etc). 

There are two major shells widely used:
- bash
- zsh

## Bash
At the beginning of each terminal session (whenever you open the terminal) a script is executed: ~/.bashrc. It's located in your home directory. This file is where we can create aliases to increase our productivity.

Some simple aliases you can add at the end of your .bashrc
```bash
alias upd="sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt autoc>autoclean -y" # to refresh your device in one line

alias desk="mv ~/Desktop/* ." # I use this one a lot. When i download something i put it in the Desktop to know what hasn't been ordered yet. Run "desk" to move all your items to your working directory. 

alias nau="nautilus ." # open nautilus on the current directory (ubuntu based file manager).
```

## Zsh
Bash is the default shell for Unix and Linux. Zsh is an improvement on Bash that can handle plugins and a bunch of extra stuff. I recommended trying out bash first and once you are comfortable you can start using zsh. However, zsh is not very useful without its framework manager Oh-my-zsh

### zsh installation and oh-my-zsh

```bash
https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH # to install zsh
https://github.com/ohmyzsh/ohmyzsh
```

## The plugins!
Once we have successfully installed Oh-my-zsh we can add plugins. 
The most important plugins that I use are:

- git 
- zsh-autosuggestions 
- zsh-syntax-highlighting

Git comes with the installation. However, you need to download the previous two. Auto suggestions is very useful to run commands very quickly. For example, you type this command:

```bash
sudo apt-get install && sudo apt-get upgrade # update your machine dude!
```
Now manually typing everything again, if we type ``sudo`` we will see an autocomplete for the previous command. This is very useful when working with large commands. If a command is repeated very often, then add it to the ~/.zshrc as an ``alias``(see Aliases). Doing so will increase your productivity!
