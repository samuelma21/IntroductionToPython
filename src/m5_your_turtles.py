"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mary Ashley Samuelson.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

sally = rg.SimpleTurtle('turtle')
pColor = ['red', 'orange', 'yellow', 'green', 'blue']
sally.speed = 25

for i in range(5):
    sally.pen = rg.Pen(pColor[i], 5)
    #draw a pentagon
    sally.pen_down()
    sally.right(72)
    sally.forward(50)
    sally.right(72)
    sally.forward(50)
    sally.right(72)
    sally.forward(50)
    sally.right(72)
    sally.forward(50)
    sally.right(72)
    sally.forward(50)

    #new pentagon starting position
    sally.pen_up()
    sally.left(72)
    sally.forward(50)

window.close_on_mouse_click()