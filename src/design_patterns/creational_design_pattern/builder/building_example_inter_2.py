class Computer(object):

    def display(self):
        print("Custom Computer:")
        print("\t{:>10}: {}".format("Case", self.case))
        print("\t{:>10}: {}".format("Mainboard", self.mainboard))
        print("\t{:>10}: {}".format("CPU", self.cpu))
        print("\t{:>10}: {}".format("Memory", self.memory))
        print("\t{:>10}: {}".format("Hard Drive", self.hard_drive))
        print("\t{:>10}: {}".format("Video Card", self.video_card))


class MyComputerBuilder(object):

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        self.get_case()
        self.mainboard()
        self.install_mainboard()
        self.hard_drive()
        self.video_card()

    def get_case(self):
        self._computer.case = "CoolerMaster N300"

    def mainboard(self):
        self._computer.mainboard = "MSI 970"
        self._computer.cpu = "Intel COre i7-4770"
        self._computer.memory = "Corsair Vengeance 16Gb"

    def hard_drive(self):
        self._computer.hard_drive = "Seagate 2TB"

    def video_card(self):
        self._computer.video_card = "GeForce GTX 1070"

    def install_mainboard(self):
        pass


if __name__ == "__main__":
    builder = MyComputerBuilder()
    builder.build_computer()
    computer = builder.get_computer()
    computer.display()
