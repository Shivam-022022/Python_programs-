class Camera:
    def take_photo(self):
        print("Camera: Photograph captured.")


class Phone:
    def make_call(self, number):
        print(f"Phone: Calling {number}...")


class Smartphone(Camera, Phone):
    def __init__(self, model):
        self.model = model


sp = Smartphone("Galaxy S25")
print("Model:", sp.model)
sp.take_photo()
sp.make_call("9876543210")
