"""
This script gives solution for a given problem statement
Flavius Josephus, a Jewish historian living in the 1st century. According to Josephus' account,
he and his 40 soldiers were trapped in a cave by Roman soldiers. They chose suicide over capture,
and decided to form a circle and commit suicide in step of three. Josephus states that by luck or
possibly by the hand of God, he and another man remained until the end and surrendered to the Romans
rather than killing themselves.

Write a documented, modular program in Python to compute the position where a person has to stand to
survive given group size of M and step of N.
"""

from cave.cave import Cave

__version__ = '1.0'
__author__ = 'Vinay Sawant'
__date__ = '2016-07-21'


if __name__ == "__main__":
    try:
        soldiers_count = int(input("Enter Soldiers count : "))
        step = int(input("Enter Step size : "))
        start_position = int(input("Enter start position : "))

        cave = Cave(soldiers_count=soldiers_count, start_position=start_position, step=step)
        cave.add_soldiers()
        cave.kill_soldiers_with_step()
        alive_soldiers = cave.get_alive_soldiers()

        print("Safe Positions  : ")
        for soldier in alive_soldiers:
            print("{0}".format(str(soldier.position)))
    except Exception as ex:
        print("Exception: {0}".format(str(ex)))
