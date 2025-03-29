# 사용자 예외처리 익셉션을 생성한다.
class InvalidParamError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)

class NoneParamError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
    
class NoneParamError1(Exception):    
    def __init__(self, msg: str):
        super().__init__(msg)
