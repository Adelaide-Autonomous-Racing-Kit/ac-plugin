import sys
import os
import platform

if platform.architecture()[0] == "64bit":
    sysdir = os.path.dirname(__file__) + "/stdlib64"
else:
    sysdir = os.path.dirname(__file__) + "/stdlib"
sys.path.insert(0, sysdir)
os.environ["PATH"] = os.environ["PATH"] + ";."

from server import AARCServer
import ac

server = None


def acMain(ac_version):
    global server
    app = ac.newApp("AARK")
    ac.setTitle(app, "  Autonomous Racing")
    ac.setSize(app, 220, 40)
    ac.drawBackground(app, 0)

    label = ac.addLabel(app, "")
    ac.setFontSize(label, 12)
    ac.setPosition(label, 5, 103)

    server = AARCServer()
    server.start()

    return "AARK"


def acUpdate(deltaT):
    # Has to be here to allow application threads to receive execution context
    return


def acShutdown(*args):
    return
