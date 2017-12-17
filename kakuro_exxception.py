class KakuroException(Exception):

    def __init__(self, msg):
        self.msg = msg


class KakuroNotSolution(KakuroException):
    pass


class GUIException(Exception):

    def __init__(self, msg):
        self.msg = msg


class NanSettingArgument(GUIException):
    pass

class IncorrectRule(GUIException):
    pass
