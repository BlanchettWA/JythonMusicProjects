# testoscjserver.py
#
# An attempt to foster connectivity between a javascript node.js application and JythonMusic
#
#

 
from osc import *
 
oscIn = OscIn( 8001 )
 
def printMessage(message):
   address = message.getAddress()
   args = message.getArguments()
   print "OSC message:", address,
   for i in range( len(args) ):
      print args[i],
   print
 
oscIn.onInput("/.*", printMessage)