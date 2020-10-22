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
Is the combination of both that allows us to run commands, for example ``dw`` which stands for *delete word*. Try this on while you follow this tutorial to get the hang of it. -> Wordthatneedstobedeleted. You need to be at the beginning of the word.

Now let's try to repeat the same command. If we are to press ``.`` Vim remembers that this is our last command and will redo it. Try it deleting this word -> secondWordTobedeleted.  

The next trick is to replace a word. We do that by preseing ``cw``. We can repeat this process again. put-your-own-word-here -> repeat-process-here.

cucumber-cucumber-cucumber-cucumber-cucumber -> cucumber-cucumber-cucumber

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
w => word (you can use this to go forward a word)
b => back (as in go back a word, Ctrl+arrows does the same)
2j => down 2 lines
``` 

Once these two modes have been stablished here are a few things we can do while in **command mode**
```vim
:q # quits
:wq # quits and saves
dd # deletes a line
/ # searches a word
```


