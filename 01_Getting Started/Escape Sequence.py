""""
/n --newline
/t --horzontal tab
/a --ascii bell
/v --vertical tab
/b --backslash
// --single slash
/" --double quote
/' --single quote
/ooo --return octal value (41 to 100) symbols and numbers(101 to 132)alphabets capital
/xhh --char with hex value (21 to 40) symbols and numbers(41 to 59 ,5A)alphabets capital
/f -- ascii formfreed
/r --carriage return
"""
print("escape this \rhello\n")
print("\t how are you\v")
print("i am um \a fine")
print("what\'s \f going on")
print("\"nothing\" What About you")
print("\110")
print("\x51")