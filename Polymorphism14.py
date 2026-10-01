class Media:
    def play(self):
        print("Playing media")


class Audio(Media):
    def play(self):
        print("Audio: Playing song through speakers...")


class Video(Media):
    def play(self):
        print("Video: Playing movie with picture and sound...")


class Podcast(Media):
    def play(self):
        print("Podcast: Playing episode with host discussion...")


for m in (Audio(), Video(), Podcast()):
    m.play()
