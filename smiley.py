from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BLANK = (0, 0, 0)

    def __init__(self, complexion=None):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        
        # Store complexion as an instance variable
        self.my_complexion = complexion if complexion is not None else self.YELLOW
        
        X = self.complexion()
        O = self.BLANK
        self.pixels = [
            O, X, X, X, X, X, X, O,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            X, X, X, X, X, X, X, X,
            O, X, X, X, X, X, X, O,
        ]
   
    def complexion(self):
        """Return the default complexion (color) of the smiley."""
        return self.my_complexion

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)


