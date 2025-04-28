from machine import Pin
from time import sleep

argon_clk = Pin(18, Pin.IN, Pin.PULL_UP)
argon_data = Pin(19, Pin.OUT, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

argon_data.value(1)

def send_to_argon(cmd):
    cmd = cmd.replace(' ', '')
    argon_data.value(0)
    for i in range(10):
        while argon_clk.value() == 1:
            pass
        argon_data.value(int(cmd[i]))
        led.value(int(cmd[i]))
        while argon_clk.value() == 0:
            pass
    print(f"Command {cmd} sent!")
    sleep(0.0025)
    argon_data.value(1)
    sleep(0.1)


def custom_christmas_lights():
    send_to_argon("0010000000")
    send_to_argon("0010000100")

    while True:
        send_to_argon("0010100110")
        send_to_argon("0010111001")
        sleep(.5)
        
        send_to_argon("0010101001")
        send_to_argon("0010110110")
        sleep(.5)

def custom_boot_anim():
    send_to_argon("0010000000")

    power_off()
    send_to_argon("0010100001")
    sleep(.1)
    send_to_argon("0010100000")
    power_on()
    sleep(.1)
    power_off()
    send_to_argon("0010101000")
    sleep(.1)
    power_off()
    send_to_argon("0010100010")
    sleep(.1)
    send_to_argon("0010100000")
    power_on()
    sleep(.1)
    power_off()
    send_to_argon("0010100100")
    sleep(.1)
    send_to_argon("0010100000")
    power_on()
    sleep(.1)
    send_to_argon("0010101111")
    sleep(.1)
    send_to_argon("0010100000")
    sleep(.1)
    send_to_argon("0010101111")
    sleep(.1)
    send_to_argon("0010100000")
    sleep(.1)
    send_to_argon("0010101111")
    sleep(.1)
    clear_led_override()
    
def custom_boot_anim2():
    send_to_argon("0010000000")

    power_off()
    send_to_argon("0010100001")
    sleep(.1)
    send_to_argon("0010100110")
    power_on()
    sleep(.1)
    power_off()
    send_to_argon("0010101000")
    sleep(.1)
    power_off()
    send_to_argon("0010100010")
    sleep(.1)
    send_to_argon("0010101001")
    power_on()
    sleep(.1)
    power_off()
    send_to_argon("0010100100")
    sleep(.1)
    send_to_argon("0010100000")
    power_on()
    sleep(.1)
    send_to_argon("0010101111")
    sleep(.1)
    send_to_argon("0010100000")
    sleep(.1)
    send_to_argon("0010101111")
    sleep(.1)
    send_to_argon("0010100000")
    sleep(.1)
    send_to_argon("0010101111")
    sleep(.1)
    clear_led_override()

def custom_boot_anim3():
    send_to_argon("0010000000")

    power_on(True)
    while True:
        send_to_argon("0010100011")
        send_to_argon("0010111010")
        send_to_argon("0010101100")
        send_to_argon("0010110101")

def custom_led_anim():
    send_to_argon("0010000000")
    send_to_argon("0010000100")

    while True:
        send_to_argon("0010101100")
        sleep(.5)
        
        send_to_argon("0010100011")
        sleep(.5)

def bind():
    send_to_argon("0000000100")

def power_on(flashing = False, anim = False):

    cmd = "001000"

    if flashing:
        cmd += "110"
    else:
        cmd += "010"

    if anim:
        cmd += "1"
    else:
        cmd += "0"

    send_to_argon(cmd)

def power_off(anim = False):
    if anim:
        send_to_argon("0010001001")
    else:
        send_to_argon("0010001000")

def lock_off():
    send_to_argon("0010000000")

def clear_led_override():
    send_to_argon("0010010000")

def argon_configure(radio = True, tilt = 0):
    cmd = "00000100"

    if radio:
        cmd += "1"
    else:
        cmd += "0"

    if tilt == 0:
        cmd += "0"
    else:
        cmd += "1"

    send_to_argon(cmd)

def mfg_test():
    send_to_argon("0011010111")

def boot_process_sim():
    clear_led_override()
    power_off()
    sleep(2)
    power_on()
    sleep(4)
    power_on(anim=True)
    sleep(7)
    send_to_argon("0010100001")

