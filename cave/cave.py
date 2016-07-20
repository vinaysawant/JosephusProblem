"""
This class is a logical representation of a Cave described in a problem statement
"""

from soldier.soldier import Soldier

__version__ = '1.0'
__author__ = 'Vinay Sawant'
__date__ = '2016-07-21'


class Cave(object):
    def __init__(self, **kwargs):
        self.soldiers = []
        self.step = kwargs.get('step')
        self.soldiers_count = kwargs.get('soldiers_count')
        self.start_position = kwargs.get('start_position')

    def add_soldiers(self):
        """
        Add N number of soldiers in a list with default is_alive status as True
        """
        for i in range(1, self.soldiers_count + 1):
            soldier = Soldier(position=i)
            self.soldiers.append(soldier)

    def get_alive_soldiers(self):
        """
        Get All Soldiers who survived in a suicide
        """
        return [soldier for soldier in self.soldiers if soldier.is_alive]

    def get_initial_kill_position(self):
        """
        Get the initial position of a soldier to kill
        """
        if self.step < self.soldiers_count:
            kill_position = self.start_position + (self.step - 1)
        else:
            kill_position = self.start_position
        return kill_position if kill_position < self.soldiers_count else kill_position - self.soldiers_count

    def get_next_position(self, index):
        """
        This method calculates the next killing position, also handles the circular movement issue
        :param index:
        :return: position (new index to kill)
        """
        count = 0
        position = 0
        index -= 1
        while self.step != count:
            new_index = index + position
            new_index = new_index if new_index <= self.soldiers_count - 1 else new_index - self.soldiers_count
            soldier = self.soldiers[new_index]
            if soldier.is_alive:
                count += 1
            position += 1
            if position > self.soldiers_count:
                break
        position += index
        return position if position < self.soldiers_count else position - self.soldiers_count

    def kill_soldiers_with_step(self):
        """
        This method traverse circular in a list and finds the safe positions
        """
        soldiers_count = self.soldiers_count
        kill_position = self.get_initial_kill_position()
        while soldiers_count >= self.step:
            soldier = self.soldiers[kill_position - 1]
            soldier.kill()
            soldiers_count -= 1
            kill_position = self.get_next_position(kill_position)
