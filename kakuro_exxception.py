class KakuroException(Exception):

    def __init__(self, msg):
        self.msg = msg


class KakuroNotSolution(KakuroException):
    pass
