class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clu=False

    def start(self):
        self.acc=True
        self.clu=True
        print("Car is starting")

    def stop(self):
        self.brk=True
        print("Car is stop")

car1=Car()
car1.start()
car1.stop()
