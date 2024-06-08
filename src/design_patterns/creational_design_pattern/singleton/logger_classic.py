"""
violates SRP
Instantiates it's own process and holds the process
Non standard class access
Harder to test
Carry global state
hard to sub class
singletons considered harmful (anti patterns)
"""


import datetime


class Logger(object):
    log_file = None
    
    @staticmethod
    def instance():
        if '_instance' not in Logger.__dict__:
            Logger._instance = Logger()
            
        return Logger._instance
    
    def open_log(self, path):
        self.log_file = open(path, mode="w")
    
    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = "%s: %s" % (now, log_record)
        self.log_file.writelines(record)
        
    def close_log(self):
        self.log_file.close()
    

if __name__ == '__main__':
    logger = Logger.instance()
    logger.open_log("my.log")
    logger.write_log("Logging with Classic Singleton Pattern")
    logger.close_log()
    
    with open("my.log", "r") as f:
        for line in f:
            print(line)