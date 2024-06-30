import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("text with help")
    print("Arguments enter " + str(sys.argv[1:]))
else:
    print("Argument NOT  PROVIDED")

os.system("dir > text.txt")

sys.exit()