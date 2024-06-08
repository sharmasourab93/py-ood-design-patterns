"""
Fix the SRP
Building a base class for all singletons
Inherit from the base class for each one
Fix Non Standard Instance access
Doesn't fixes
    - Testing
    - Global state
    - Maintainance
"""

import datetime


class Singleton(object):
    _instances = {}  # dict ([cls, instance])

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Logger(Singleton):
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
    logger = Logger("my.log")
    logger.write_log("Logging with classic Singleton Pattern")
    logger2 = Logger("***ignored***")
    logger2.write_log("Another log record")

    logger.close_log()

    with open("my.log", "r") as f:
        for line in f:
            print(line, end=" ")
