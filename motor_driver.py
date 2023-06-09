from machine import Pin, PWM


class L298N:
    def __init__(self, in1_pin, in2_pin, ena_pin, in3_pin, in4_pin, enb_pin):
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        self.ena = PWM(Pin(ena_pin))
        self.ena.freq(1000)
        self.in3 = Pin(in3_pin, Pin.OUT)
        self.in4 = Pin(in4_pin, Pin.OUT)
        self.enb = PWM(Pin(enb_pin))
        self.enb.freq(1000)
        self.channel_a_off()
        self.channel_b_off()
    
    @staticmethod
    def get_duty_cycle(speed):
        if speed < 0:
            raise ValueError('Speed must be Greater than 0')
        
        if speed > 100:
            raise ValueError('Speed must be Less than 100')
        
        return int((speed/100)*65535)

    def channel_a_clockwise(self, speed = 50):
        self.ena.duty_u16(L298N.get_duty_cycle(speed))
        self.in1.on()
        self.in2.off() 
    
    def channel_a_anticlockwise(self, speed = 50):
        self.ena.duty_u16(L298N.get_duty_cycle(speed))
        self.in1.off()
        self.in2.on() 
    
    def channel_a_off(self):
        self.in1.off()
        self.in2.off() 
    
    def channel_b_clockwise(self, speed = 50):
        self.enb.duty_u16(L298N.get_duty_cycle(speed))
        self.in3.on()
        self.in4.off()
    
    def channel_b_anticlockwise(self, speed = 50):
        self.enb.duty_u16(L298N.get_duty_cycle(speed))
        self.in3.off()
        self.in4.on()
    
    def channel_b_off(self):
        self.in3.off()
        self.in4.off()
        
    def deinit(self):
        self.channel_a_off()
        self.channel_b_off()
        self.ena.deinit()
        self.enb.deinit()

class L298NSingleChannel:
    def __init__(self, in1_pin, in2_pin, ena_pin):
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        self.ena = PWM(Pin(ena_pin))
        self.ena.freq(1000)
        self.channel_a_off()
    
    @staticmethod
    def get_duty_cycle(speed):
        if speed < 0:
            raise ValueError('Speed must be Greater than 0')
        
        if speed > 100:
            raise ValueError('Speed must be Less than 100')
        
        return int((speed/100)*65535)

    def channel_a_clockwise(self, speed = 50):
        self.ena.duty_u16(L298N.get_duty_cycle(speed))
        self.in1.on()
        self.in2.off() 
    
    def channel_a_anticlockwise(self, speed = 50):
        self.ena.duty_u16(L298N.get_duty_cycle(speed))
        self.in1.off()
        self.in2.on() 
    
    def channel_a_off(self):
        self.in1.off()
        self.in2.off() 
        
    def deinit(self):
        self.channel_a_off()
        self.ena.deinit()