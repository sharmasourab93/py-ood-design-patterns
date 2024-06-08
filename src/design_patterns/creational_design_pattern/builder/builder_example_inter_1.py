"""
Too Many parametes fixed
Attributes are encapsulated

Ordering Problem still exists 
"""

class Computer(object):

    def display(self):
        print("Custom Computer:")
        print("\t{:>10}: {}".format("Case", self.case))
        print("\t{:>10}: {}".format("Mainboard", self.mainboard))
        print("\t{:>10}: {}".format("CPU", self.cpu))
        print("\t{:>10}: {}".format("Memory", self.memory))
        print("\t{:>10}: {}".format("Hard Drive", self.hard_drive))
        print("\t{:>10}: {}".format("Video Card", self.video_card))


class MyComputer(object):
    
    def get_computer(self):
        return self._computer
    
    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = "CoolerMaster N300"
        computer.mainboard = "MSI 970"
        computer.cpu = "Intel COre i7-4770"
        computer.memory = "Corsair Vengeance 16Gb"
        computer.hard_drive = "Seagate 2TB"
        computer.video_card = "GeForce GTX 1070"


if __name__ == '__main__':
    builder = MyComputer()
    builder.build_computer()
    computer = builder.get_computer()
    computer.display()
