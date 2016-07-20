from soldier.soldier import Soldier


class Cave(object):
    def __init__(self, **kwargs):
        self.soldiers = []
        self.step = kwargs.get('step')
        self.soldiers_count = kwargs.get('soldiers_count')
        self.start_position = kwargs.get('start_position')

    def add_soldiers(self):
        for i in range(1, self.soldiers_count + 1):
            soldier = Soldier(position=i)
            self.soldiers.append(soldier)

    def get_alive_soldiers(self):
        return [soldier for soldier in self.soldiers if soldier.is_alive]

    def get_initial_kill_position(self):
        if self.step < self.soldiers_count:
            kill_position = self.start_position + (self.step - 1)
        else:
            kill_position = self.start_position
        return kill_position if kill_position < self.soldiers_count else kill_position - self.soldiers_count

    def get_next_position(self, index):
        count = 0
        positions = 0
        index -= 1
        while self.step != count:
            new_index = index + positions
            new_index = new_index if new_index <= self.soldiers_count - 1 else new_index - self.soldiers_count
            soldier = self.soldiers[new_index]
            if soldier.is_alive:
                count += 1
            positions += 1
            if positions > self.soldiers_count:
                break
        positions += index
        return positions if positions < self.soldiers_count else positions - self.soldiers_count

    def kill_soldiers_with_step(self):
        soldiers_count = self.soldiers_count
        kill_position = self.get_initial_kill_position()
        while soldiers_count >= self.step:
            soldier = self.soldiers[kill_position - 1]
            soldier.kill()
            soldiers_count -= 1
            kill_position = self.get_next_position(kill_position)
