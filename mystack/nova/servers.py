"""
"""

class ServerController(object):
    def __init__(self):
        pass

    def __call__(self):
        pass

    def show(self):
        print '[DEBUG] call ServerController.show'
        return "call ServerContoller.show"


def createresource():
    return ServerController()
