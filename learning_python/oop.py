class Starship(object):
    sound = 'vrrrr'

    def __init__(self):
        self.engines = False
        self.engine_speed = 0
        self.shields = True
        self.__self_destruct = False #private field
        self.__captain: str = None

    def engage(self):
        self.engines = True

    def warp(self, factor: int):
        self.engine_speed = 2
        self.engine_speed *= factor

    @property
    def captain(self)-> str:
        return self.__captain

    @property
    def captain(self, name: str):
        self.__captain = name

    @classmethod
    def make_sound(cls):
        print(cls.sound)

    def __str__(self):
        return f'engine: {self.engines}, engine speed: {self.engine_speed}, shield: {self.shields}'



if __name__ == "__main__":
    s = Starship()
    print(1,s)

    s.warp(4)
    print(2, s)

    s.engage()
    print(3, s)

    # you can't really access private instance variables from the outside, for instance using self.__self_destruct
    # you actually can, however using name mangling
    # accessing private field using name mangling
    print(s._Starship__self_destruct)

    # class method
    Starship.make_sound()
