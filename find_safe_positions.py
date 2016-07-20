from cave.cave import Cave

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
