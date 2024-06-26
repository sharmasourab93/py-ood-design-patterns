"""

"""


class Computer(object):
    def __init__(self, case, mainboard, cpu, memory, hard_drive, video_card):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive
        self.video_card = video_card

    def display(self):
        print("Custom Computer:")
        print("\t{:>10}: {}".format("Case", self.case))
        print("\t{:>10}: {}".format("Mainboard", self.mainboard))
        print("\t{:>10}: {}".format("CPU", self.cpu))
        print("\t{:>10}: {}".format("Memory", self.memory))
        print("\t{:>10}: {}".format("Hard Drive", self.hard_drive))
        print("\t{:>10}: {}".format("Video Card", self.video_card))


if __name__ == "__main__":
    computer = Computer(
        case="CoolerMaster N300",
        mainboard="MSI 970",
        cpu="Intel COre i7-4770",
        memory="Corsair Vengeance 16Gb",
        hard_drive="Seagate 2TB",
        video_card="GeForce GTX 1070",
    )

    computer.display()
