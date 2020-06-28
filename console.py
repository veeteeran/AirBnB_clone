#!/usr/bin/python3
""" A CLI for HolBnb """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The top class for our CLI """

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_exit(self, *args):
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

    def do_create(self, class_name):
        """
        Creates a new instance of BaseModel
        """

        if class_name is None:
            print("** class name missing **")
            pass
        elif not isInstance(class_name, BaseModel):
            print("** class doesn't exist **")
            pass

        new_obj = BaseModel()
        new_obj.save()

    def do_show(self, class_name, uuid):
        """
        Print class name and uuid
        """
        if class_name is None:
            print("** class name missing **")
            pass
        elif not isInstance(class_name, BaseModel):
            print("** class doesn't exist **")
            pass
        elif uuid is None:
            print("** instance id missing **")
            pass

        all_objs = storage.all()
        key = class_name + '.' + uuid
        if key in all_objs:
            my_obj = BaseModel(all_obj[key])
            print(my_obj)
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
