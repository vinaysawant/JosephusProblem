"""
This class is a logical representation of a Soldier described in a problem statement
"""

__version__ = '1.0'
__author__ = 'Vinay Sawant'
__date__ = '2016-07-21'


class Soldier(object):
    def __init__(self, **kwargs):
        self.position = kwargs.get('position')
        self.is_alive = True

    def kill(self):
        """
        Set is_alive flag of a soldier to False
        """
        self.is_alive = False
        print("Killed soldier at position : {0}".format(str(self.position)))
