class Tardis(object):

    def __init__(self):
        super().__init__()

    def camouflage(self):
        raise NotImplementedError('You should implement this in a subclass')

class TardisChild(Tardis):
    def camouflage(self):
        return 'Yay! Overridden'

if __name__ == "__main__":

    # Will raise exception
    # tardis = Tardis()
    # tardis.camouflage();

    child = TardisChild()
    print(child.camouflage())
