from Controller import Controller


class LEDController(Controller):
    def __init__(self, led_list, length, IP_address, controller_hardware):
        self.led_list = led_list
        self.length = length
        self.IP_address = IP_address
        self.controller_hardware = controller_hardware # Arduino or RAspi??

