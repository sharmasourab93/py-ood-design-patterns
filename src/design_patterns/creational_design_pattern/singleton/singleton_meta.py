import datetime


class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance

        return cls._instance[cls]


# Separation of Concerns (SoCs) complete
class Logger(metaclass=Singleton):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode="w")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = "%s: %s\n" % (now, log_record)
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


if __name__ == "__main__":
    if __name__ == "__main__":
        logger = Logger("my.log")
        logger.write_log("Logging with classic Singleton Pattern")
        logger2 = Logger("***ignored***")
        logger2.write_log("Another log record")

        logger.close_log()

        with open("my.log", "r") as f:
            for line in f:
                print(line, end=" ")
