#!/usr/bin/python3
""" A CLI for HolBnb """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


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

    def do_create(self, *args):
        """
        Creates a new instance of BaseModel
        """

        if args[0] is None:
            print("** class name missing **")
            pass
        elif not isInstance(args[0], BaseModel):
            print("** class doesn't exist **")
            pass

        new_obj = BaseModel()
        new_obj.save()

    def do_show(self, *args):
        """
        Print class name and uuid
        """
        if args[0] is None:
            print("** class name missing **")
            pass
        elif not isInstance(args[0], BaseModel):
            print("** class doesn't exist **")
            pass
        elif args[1] is None:
            print("** instance id missing **")
            pass

        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key in all_objs:
            my_obj = BaseModel(all_obj[key])
            print(my_obj)
        else:
            print("** no instance found **")

    def do_destroy(self, *args):
        """
        Deletes an instance based on the class name and id

            Parameters:
                class_name: name of the class
                uuid: id of object
        """
        if args[0] is None:
            print("** class name missing **")
            pass
        elif not isInstance(args[0], BaseModel):
            print("** class doesn't exist **")
            pass
        elif args[1] is None:
            print("** instance id missing **")
            pass

        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key in all_objs:
            my_obj = BaseModel(all_obj[key])
            del my_obj
        else:
            print("** no instance found **")

    def do_all(self, *args):
        """
        Prints all string representation of all instances

            Parameter:
                args: name of class, optional parameter
        """
        if not isInstance(args[0], BaseModel):
            print("** class doesn't exist **")
            pass
        elif args[0] is BaseModel or args[0] is None:
            all_objs = storage.all()
            my_list = []
            for key in all_objs:
                my_obj = BaseModel(all_objs[key])
                my_list.append(my_obj.__str__)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
