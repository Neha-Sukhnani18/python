class Emplyee:
    def __init__(self):
        print('emplyee created.')
    def __del__ (self):
        print('destructor called, emplyee deleted')

obj = Emplyee()
del obj 