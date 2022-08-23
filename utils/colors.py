import random

class ColorMaker:
    @staticmethod
    def make_color_rgb():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))