# ledring
Application to control 8 led lights from a rasberry py (4)
# Functionlity 
On start up the app will execute a little 'hello world' sequence for a few seconds.
After that all led will be turned off, and the app waits for a buttton push.
For every push the app will step through all the 8 led's + an off state in a circular manner

# Used HW

See: https://www.mouser.se/datasheet/2/1376/8_MOSFETS_UsersGuide-3003107.pdf

# Push button 
Push button to be connected to pin 37 of the Raspberry Pi GPIO connector (GPIO26),
and should connect that down gnd when pushed.
Until that is connected the button marked 'rst' on the mosfet card can be used

# Deployment
The app is tested running Ubuntu 22.04 & Python 3.10.
It is intended to run as a service using root rights.
For details see folder 'service_files'

Before deployed as a service, the app must be  packed to a 'one file' executable.
To do that run the './pack.sh' command. This will create the executable file in ./dist
