COLORS = { \
    #Colors
    "black": "\033[1;30;48m",  # Black bold
    "red": "\033[1;31;48m",  # Red bold
    "green": "\033[1;32;48m",  # Green bold
    "yellow": "\033[1;33;48m",  # Yellow bold
    "blue": "\033[1;34;48m",  # Blue bold
    "magenta": "\033[1;35;48m",  # Magenta bold
    "cyan": "\033[1;36;48m",  # Cyan bold
    "white": "\033[1;37;48m",  # White bold 
    "br": "\033[0m",  # closeColor
    "reset": "\u001b[0m",  # unicode
    "hxdc": "\x1b[0m", # Hexdecimal
    
    #Background Color
    "bblack": "\033[1;34;40m",  # Black
    "bred": "\033[1;34;41m",  # Red
    "bgreen": "\033[1;34;42m",  # Green
    "byellow": "\033[1;34;43m",  # Yellow
    "bblue": "\033[1;34;44m",  # Blue
    "bmagenta": "\033[1;34;45m",  # Magenta
    "bcyan": "\033[1;34;46m",  # Cyan
    "bwhite": "\033[1;34;47m",  # White
  
    #Fonts
    #0 - Normal
    #1 - Bold
    #2 - Light
    #3 - Italicized
    #4 - Underlined
    #5 - Blink
    #Test color : print(CL(" [yellow] COLOR YELLOW] "))
    # Test Background Color: print(CL(" [byellow] Background Color Yellow "))
    
    
    
}
def CL(text):
    for color in COLORS:
        text = text.replace("[" + color + "]", COLORS[color])
    return text
    
    