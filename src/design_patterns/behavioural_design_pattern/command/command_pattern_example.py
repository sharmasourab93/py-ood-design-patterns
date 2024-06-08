"""
Violates SRP
Violates Open/Close Principle
Violates DIP
Violates Long List of if/elif clauses
"""
import sys


class CommandExecutor(object):
    
    def execute_command(self, args):
        if args[0] == "CreateOrder":
            self.create_order()
        elif args[0] == "update_quantity":
            self.update_quantity(args[1])
        elif args[0] == "ShipOrder":
            self.ship_order()
        else:
            print("Unrecognized command: " + args[0])
    
    def create_order(self):
        pass
    
    def update_quantity(self, val):
        print(val)
        old_val = 5
        print("Database Updated")
        print("Loggin Updated quantity from %s to %s" % (old_val, val))
        
    def ship_order(self):
        pass


if __name__ == '__main__':
   
   if len(sys.argv) < 2:
       print("Usage:" + r"C:\Users\Sourab Sharma\AppData\Local\Programs\Python\Python36\python -m BeforeCommand <command>")
       print("Commands:")
       print("\t Create order")
       print("\t update_quantity number")
       print("\t ShipOrder")
       exit()
       
   executor = CommandExecutor()
   executor.execute_command(sys.argv[1:])
