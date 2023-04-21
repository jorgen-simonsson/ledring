
''' App to handle 8 led lights '''
import time
import lib8mosind
import RPi.GPIO as gpio


BUTTON_CHANNEL = 26
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
        self.light_index = 8

        # Init the button port as input with pull up
        gpio.setmode(gpio.BCM)
        gpio.setup(BUTTON_CHANNEL, gpio.IN, pull_up_down=gpio.PUD_UP)


    def debounced_state(self):
        counter = 0
        state = gpio.input(BUTTON_CHANNEL)
        # wait for 50ms
        time.sleep(0.05)
        # check the input pin 40 times in 1ms intervals
        for i in range(40):
            if gpio.input(BUTTON_CHANNEL) != state:
                counter = 0
                state = gpio.input(BUTTON_CHANNEL)
            else:
                counter += 1
            time.sleep(0.001)
            # if the input has been stable for 20ms, return the value
            if counter >= 20:
                return state

    def step(self):
        self.all_off()
        self.light_index = self.light_index +1
        if self.light_index > 8:
            self.light_index =0
        if self.light_index < 8:
            lib8mosind.set(self.lights[self.light_index].card,self.lights[self.light_index].led_number,ON)    

    def all_off(self):
        lib8mosind.set_all(FIRST_CARD, 0)
        lib8mosind.set_all(SEC_CARD, 0)

    def show_off(self):
        show_cnt=2
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
        self.all_off()

light = Light()
light.show_off()
old_state = light.debounced_state()
while True:
    new_state = light.debounced_state()
    if new_state != old_state:
        if new_state == 1:
            light.step()
    old_state = new_state

