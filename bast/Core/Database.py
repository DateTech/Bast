import datetime
import time
import os

class Migration:
    def generate(self, args):
        if args.g[0] == 'create:migration' and type(args.g[1]) == str:
            filename = args.g[1] + datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
            self.migration_creator(filename)
            print("\033[1;32;40m Migrations/" + filename + " Migration generated successfully")
        else:
            print("\033[1;31;40m Command not found ")
            os.system("bast -h")

    def migration_creator(self, filename):
        file_name = str(filename+'.py')
        file_migrate = open('bast/Migrations/'+file_name, 'w+')
        compose = "def "+filename+"():\n\tprint 'Hello world'"
        file_migrate.write(compose)
        file_migrate.close()