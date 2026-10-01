class SmartDevice:
    def turn_on(self):
        print("Device ON")

    def turn_off(self):
        print("Device OFF")


class Light(SmartDevice):
    def turn_on(self):
        print("Light: Bulb glows bright.")

    def turn_off(self):
        print("Light: Bulb switched off.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan: Blades start rotating.")

    def turn_off(self):
        print("Fan: Blades slow down and stop.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC: Compressor starts, room begins cooling.")

    def turn_off(self):
        print("AC: Cooling stopped.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV: Screen lights up and channels appear.")

    def turn_off(self):
        print("TV: Screen goes dark.")


for d in (Light(), Fan(), AC(), TV()):
    d.turn_on()
    d.turn_off()
    print("-" * 30)
