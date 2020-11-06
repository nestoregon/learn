# Learning Vim

Include tricks for learning VIM. The most important part is the documentation in this project which showcases my progress when learning to use Vim.

Vim is aimed to change code rather than to code from scratch.

## Basics Controls

There are 2 editor modes:
- command
- insert

To jump to insert press ``esc`` and to jump to insert press ``i``. Note that all the shortcuts are pressed from **command** mode, to actually write something you need to go into **insert** mode.

# Basic notions
While in command come, vim operates with two things:
- actions
- words

Actions go first and then words.
Is the combination of both that allows us to run commands, for example ``dw`` which stands for *delete word*. Try this on while you follow this tutorial to get the hang of it. -> Wordthatneedstobedeleted. You need to be at the beginning of the word.

Now let's try to repeat the same command. If we are to press ``.`` Vim remembers that this is our last command and will redo it. Try it deleting this word -> secondWordTobedeleted.  

The next trick is to replace a word. We do that by pressing ``cw``. We can repeat this process again. Put-your-own-word-here -> repeat-process-here.

Potato-potato-potato-potato-potato -> potato-potato-potato 
## Basic actions
```vim
d => delete
c => change
> => indent
v => visual change
y => yank (copy)
```

## Basic nouns
```vim
w => word (you can use this to hello forward a word)
b => back (as in go back a word, Ctrl+arrows does the same)
2j => down 2 lines
``` 
## Basic Text objects
```vim
iw => "inner word" (works from anywhere in a word)
it => "inner tag" (the contents of HTML tag)
i" => "inner quotes"
ip => "inner paragraph"
as => "a sentence"
```

## Basic Parameterized Text Objects
```vim
f, F => "find" the next character
t, T => "find" the next character
/    => Search
```

## Moving through lines
```vim
h => left arrow
k => up
j => down
l => right arrow
b => previous word
w => next word
gg => go to the top of the document
yy => copy the whole line
V => visually select the whole line
G => go to the bottom of the document
```

> Change the function
> def function:
> 	input("estoy")
Once these two modes have been established here are a few things we can do while in **command mode**
```vim
:q # quits
:wq # quits and saves
dd # deletes a line
/ # searches a word
```

The built in "vimtutor" is a great tutorial.

```bash
./use_vimtutor.sh #or vimututor directly on your terminal
```
Another great tutorial is "vim genius" found on the web.

Another especially useful thing is to instead of pressing "esc" every time when we want to exit -- INSERT -- we can do ``ctrl+[``. This is way quicker!

Useful links to see:
https://realpython.com/vim-and-python-a-match-made-in-heaven/#syntax-checkinghighlighting
https://vimawesome.com/plugin/markdown-syntax for markdown!.

### Plugins

Plugins are a great way to improve your vim experience. The one I came across is Vundle. What are useful pluggins? 
The most useful plugin I have found is "autocorrections" for when you code. I wanted something similar to VSCode.

You can checkout the Vundle project [here](https://github.com/VundleVim/Vundle.vim)

### Practicing

The best way to practice is to create a file as you would normally do using vim. There you would realize what shortcuts you want to know and you can look them up. There are basic commands that we don't think we're going to use but that when you actually start coding miss. A great tool was following ``vimtutor`` and getting used to using the arrows (I still get confused sometimes especially with ``h`` and ``l``). Inserting lines above and below with ``O`` and ``o`` respectively, ``dd`` to delete a line, ``Ctrl + [`` as ``esc`` given that is more comfortable for me.   
Overall I found that learning vim is all about practicing. I still have a lot to learn but I believe that within 1 week I am able to comfortably edit a file as I would do in Visual Studio Code. Still, I have so much to learn, like for example how to manage different files at the same time given that that is something that I use quite often.

# Journal
- Day 3: After editing some files I realized what I am missing out compared to VSCode. For instance, when editing a file, it is very convenient to use ``cw`` to change the actual word, although you need to be at the beginning of this one. A Much better shortcut for this is ``ciw`` which deletes the whole world no matter in which letter the cursor is located. 
- Day 4: I realized that having autosuggestion enabled really diminishes the performance of vim. We're talking about sudden lag, getting stuck not seeing were the cursor is etc. This is surprising because it is a light editor and I thought it was going to handle an autosuggestion engine. Be aware that some installations don't come with vim installed.
- Day 5: After using the keys for a while i realized that some other well known apps (such as Gmail) have the same functionality for ``j`` and ``k``. I personally wasn't aware of the influence of vim in other apps. You can also find it in ``evince``, the pdf manager for Ubuntu. You can scroll through the pages using the same keys. I found annoying that there is no shortcut for inserting a blank space without going into insert mode, I might do it myself.
- Day 6: I found it useful the ``cib`` which stands for "change inner block". I believe that this is one of the most useful ones when you want to erase something inside quotes. Similarly, if we want to change everything inside quotes we can type ``ci"``. You get the gist of it. Extremely useful given it doesn't matter where in you are.
- Day 7: Vim is a tool and as a tool it should be used whenever the situation demands it. I am still more comfortable using VSCode, some other times for quick scripting i find Vim more useful. The key is not to use Vim for the sake of using Vim but because it is the appropriate.
- Day 8: Used Vim to write some instructions quickly but it took me more than I expected. When in --INSERT-- mode you cannot move with `hjkl`, makes sense because otherwise you would type those letters, but it is annoying to constantly change between that and -- NORMAL -- mode.
- Day 9: Becoming more used to coding in Vim for its shortcuts. Once you get used to them they become comfortable. It is however not that comfortable to use `esc` once you want to move through lines. It is quite useful to edit some code every day to improve your coding SPEED and PRODUCTIVITY
- Day 10: Talking with a colleague of mine, he recommended several plugins that I will try later such as: zathura, zinitplug and NERDTree
- Day 11: I had to install a plugin for c++ syntax highlighting because the default one wasn't accurate
