import time
from smiley import Smiley
from blinkable import Blinkable

class Angry(Smiley):
    def __init__(self):
    
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws an angry mouth (frowning line)
        """
        mouth = [49, 50, 51, 52, 53, 54]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, furrowed=True):
        """
        Draws eyes. Optionally furrowed to enhance angry expression.
        :param furrowed: If True, draw eyebrows for angry look
        """
        eye_pixels = [10, 13, 18, 21]
        for pixel in eye_pixels:
            self.pixels[pixel] = self.BLANK 

        if furrowed:
            eyebrow_pixels = [2, 3, 5, 6]
            for pixel in eyebrow_pixels:
                self.pixels[pixel] = self.BLANK

    def blink(self, delay=0.5):
        """
        Blinks the smiley's eyes once
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(furrowed=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(furrowed=True)
        self.show()
