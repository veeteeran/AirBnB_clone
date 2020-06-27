#!/usr/bin/python3
""" A CLI for HolBnb """
import cmd


class HBNBCommand(cmd.Cmd):
    """ The top class for our CLI """
    
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_exit(self,*args):
        """
        Type exit to exit the program
        """
        return True

    def do_quit(self, *args):
        """
        Type quit to exit the program
        """
        return True
    
    def do_EOF(self, line):
        """
        Type ctrl + D to exit the programm
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
