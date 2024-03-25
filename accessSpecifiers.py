class Car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside Car Constructor")

    def publicMethod(self):
        print("Inside Public Method")

    def _protectedMethod(self):
        print("Inside Protected Method")

    def __privateMethod(self):
        print("Inside Private Method")
