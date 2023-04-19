
''' App to handle 8 led lights '''
import time
import lib8mosind



FIRST_CARD = 0
SEC_CARD = 2
ON = 1
OFF = 0

class Led:
    def __init__(self, card, led_number ):
        self.card = card
        self.led_number = led_number


class Light:
    def __init__(self):
        self.lights= []
        self.lights.append(Led(FIRST_CARD,1))
        self.lights.append(Led(FIRST_CARD,2))
        self.lights.append(Led(FIRST_CARD,3))
        self.lights.append(Led(FIRST_CARD,4))
        self.lights.append(Led(SEC_CARD,1))
        self.lights.append(Led(SEC_CARD,2))
        self.lights.append(Led(SEC_CARD,3))
        self.lights.append(Led(SEC_CARD,4))
        self.light_index = 0

    def all_off(self):
        lib8mosind.set_all(FIRST_CARD, 0)
        lib8mosind.set_all(SEC_CARD, 0)

    def show_off(self):
        show_cnt=10
        self.all_off()
        index = 0
        while show_cnt >0:
            index =0
            while index <8:
                lib8mosind.set(self.lights[index].card,self.lights[index].led_number,ON)
                time.sleep(0.1)
                self.all_off()
                index = index+ 1
            show_cnt = show_cnt -1


light = Light()
light.show_off()


