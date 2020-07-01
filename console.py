#!/usr/bin/python3
""" A CLI for HolBnb """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """ The top class for our CLI """

    prompt = '(hbnb) '
    class_list = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Reprompt on empty line
        """
        pass

    def do_exit(self, arg):
        """
        Type exit to exit the program
        """
        return True

    def do_quit(self, arg):
        """
        Type quit to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Type ctrl + D to exit the programm
        """
        if not sys.stdin.isatty():
            print()

        return True

    def do_create(self, s):
        """
        Creates a new instance of BaseModel
        """
        """
        if not sys.stdin.isatty():
            print()
        """
        if s is "":
            print("** class name missing **")
        elif s in self.class_list:
            new_obj = eval(s + '()')
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, s):
        """
        Print class name and uuid
        """
        """
        if not sys.stdin.isatty():
            print()
        """
        args = s.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + '.' + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, s):
        """
        Deletes an instance based on the class name and id

        """

        if not sys.stdin.isatty():
            print()

        args = s.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + '.' + args[1]
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, s):
        """
        Prints all string representation of all instances

            Parameter:
                args: name of class, optional parameter
        """
        """
        if not sys.stdin.isatty():
            print()
        """
        args = s.split()
        my_list = []
        all_objs = storage.all()
        if len(args) == 0:
            for key in all_objs:
                my_list.append(all_objs[key].__str__())
            print(my_list)
        else:
            if args[0] in self.class_list:
                for key in all_objs:
                    if args[0] in key:
                        my_list.append(all_objs[key].__str__())
                print(my_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, s):
        """
        Updates an instance based on the class name
        """
        """
        if not sys.stdin.isatty():
            print()
        """
        args = s.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + '.' + args[1]
            if key in all_objs:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    obj_dict = all_objs[key].to_dict()
                    my_obj = all_objs[key]
                    if args[2] in obj_dict:
                        cast = type(my_obj.args[3])
                        cast(args[3])
                    setattr(my_obj, args[2], args[3])
                    my_obj.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
