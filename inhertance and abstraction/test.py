class mum:
    def __init__(self, nose, behavior):
        self.nose=nose
        self.behavior=behavior

    def display(self):
        print("your nose shape is",self.nose)
        print("your behavior is calm",self.behavior)

class daughter(mum):
    def __init__(self,name,age,nose,behavior):
        self.name=name
        self.age=age

        mum.__init(self,nose,behavior)

obj = daughter("rose",16,"round","true")
obj.display()