
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

DEBUG = "DEBUG | "

# Author: Alirezarpi

# ---------------> Desktop Reminder <-----------------

print("\033[1;37mRemember to... ?\033[0;36m\nText To Remember: ( Sentence Splited by - (dash) )\033[34m ", end="")
text = input()
print("\033[00m", end="")

count = text.count("-")
text = text.replace("-", "\n")

if ( count > 1 ):
    positionR = (100, 270) # Set position upper
    position = (120, 420)  # <-)
else:   
    positionR = (150, 370) # Set position middle of photo
    position = (170, 500)  # <-)


path = os.popen('pwd').read() # Path to image folder
path = list(path.split("\n"))
del path[-1] # Delete \n end of path

img = Image.open(''.join(path) + '/template.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(''.join(path) + '/Calibri.ttf', 70)
# draw.text((x, y), "text", (color), font)
draw.text(positionR, "Remember to...", (46,56,63), font=font)
draw.text(position, text, (46,56,63), font=font)
img.save(''.join(path) + '/rtw.jpg')
# Set as background
status = os.system("gsettings set org.gnome.desktop.background picture-uri file:{}/rtw.jpg".format(''.join(path)))

if ( status == 0 ):
    print("\033[32mSuccessfull, Check your desktop\033[00m")
else:
    print("\033[31mUnsuccessfull, I don't know why you find out yourself\033[00m")
