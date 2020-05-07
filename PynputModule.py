'''
This library allows you to control and monitor input devices. Each supported device
is a subpackage. For example, mouse is a subpackage that contains classes
for controlling and monitoring the mouse while keyboard contains classes for controlling and
monitoring the keyboard.
'''

'''
CHALLENGE: Have a website that when you open it in the browser it subscribes to this channel LOL
'''

'''
Controlling the user's mouse.
'''
from pynput.mouse import Button, Controller, Listener

mouse = Controller()    ##mouse is an instance of the controller class.

#mouse.position shows the current position of the mouse.
#Note that the top left of the monitor is 0, 0.
#The bottom right of the monitor is 1920, 1080 for 1080p screens.
'''
while True:
    print("The position of the mouse is " + str(mouse.position))
'''

#This sets the position of the mouse to the following pixels. (x, y).
'''
mouse.position = (1900, 1070)
print("The position of the mouse is now " + str(mouse.position))
'''

#This moves the mouse pointer relative to the current position.
#Specifically, here it is 100 pixels right and down.
'''
mouse.move(100, 150)
'''

#Perform a mouse click. Note that if you don't release it will highlight everything as if you're holding down the clicker.
'''
mouse.press(Button.left)
mouse.release(Button.left)
'''

#Double click, this will highlight whatever line you are on or highlight the whole page if a blank line.
'''
mouse.click(Button.left, 2)
'''

#Scrolls two steps to the right and 4 steps down.
'''
mouse.scroll(2, -4)
'''











