class Soldier(object):
    def __init__(self, **kwargs):
        self.position = kwargs.get('position')
        self.is_alive = True

    def kill(self):
        """
        Set is_alive flag of a soldire to False
        """
        self.is_alive = False
        print("Killed soldier at position : {0}".format(str(self.position)))
