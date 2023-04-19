import lib8mosind
import time

CARD = 2


lib8mosind.get_all(CARD)
lib8mosind.set_all(CARD, 0)

lib8mosind.set(CARD,8,1)
while True:
    lib8mosind.set(CARD,8,1)
    time.sleep(0.1)
    lib8mosind.set(CARD,8,0)
    time.sleep(0.1)
