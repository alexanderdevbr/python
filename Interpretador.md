# Utilizando Interpretador Python

## Limpando tela
```Python
cls = lambda: print("\033[H\033[J", end="")
cls()
```

### UPDATE 1:
Since this answer gets some attention, you might want to know how it works. The command above prints [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code):

``\033`` stands for ESC (ANSI value 27).
``\033[`` is a special [escape sequence](https://en.wikipedia.org/wiki/ANSI_escape_code#Fe_Escape_sequences) called [Control Sequence Introducer](https://en.wikipedia.org/wiki/ANSI_escape_code#CSIsection) (CSI).
``\033[H`` command moves the cursor to the top left corner of the screen.
``\033[J`` clears the screen from the cursor to the end of the screen.

Optional parameter ``end=""`` avoids printing newline character after executing these commands, so >>> stays in the topmost row.

### UPDATE 2:
You may want to extend the above command with one additional parameter - x (before J):
```
print("\033[H\033[xJ", end="")

    If x is 1, it will clear from cursor to beginning of the screen.
    If x is 2, it will clear entire screen and move cursor to upper left.
    If x is 3, it will clear entire screen and DELETE ALL LINES SAVED IN THE SCROLLBACK BUFFER.
```

So, this command will clear everything, including buffer:
```
print("\033[H\033[3J", end="")
```

### COMMAND LINE:
To clear screen in a shell (console / terminal) you can use the same command. To clear entire screen and delete all lines saved in the scrollback buffer put 3 before J:
```
printf "\033[H\033[3J"
```
or create an alias:
```
alias cls='printf "\033[H\033[3J"'
```