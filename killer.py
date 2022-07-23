import os
def kill(proc):
    os.system("kill $(pidof " + proc + ")")