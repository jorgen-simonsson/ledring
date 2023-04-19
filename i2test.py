import lib8mosind
import time

lib8mosind.get_all(0)
lib8mosind.set_all(0, 0)

lib8mosind.set(0,8,1)
while True:
    lib8mosind.set(0,8,1)
    time.sleep(0.1)
    lib8mosind.set(0,8,0)
    time.sleep(0.1)

    