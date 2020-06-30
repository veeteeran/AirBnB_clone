#!/usr/bin/python3
""" A CLI for HolBnb """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The top class for our CLI """

    prompt = '(hbnb) '
    class_list = ["BaseModel", "User"]

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

    def do_create(self, s):
        """
        Creates a new instance of BaseModel
        """
        if s is None:
            print("** class name missing **")
            pass
        elif s not in self.class_list:
            print("** class doesn't exist **")
            pass

        new_obj = BaseModel()
        new_obj.save()

    def do_show(self, s):
        """
        Print class name and uuid
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
                my_obj = BaseModel(all_objs[key])
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
        elif args[0] not in self.class_list:
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
        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            pass
        elif args[0] is "BaseModel" or args[0] is None:
            all_objs = storage.all()
            my_list = []
            for key in all_objs:
                my_obj = BaseModel(all_objs[key])
                my_list.append(my_obj.__str__)

    def do_update(self, *args):
        if args[0] is None:
            print("** class name missing **")
        if args[0] not in self.class_list:
            print("** class doesn't exist **")
            pass
        if len(args) < 2:
            print("** instance id missing **")
            pass
        if len(args) < 3:
            print("** attribute name missing **")
            pass
        if len(args) < 4:
            print("** value missing **")
            pass

        all_objs = storage.all()
        update_key = args[0] + '.' + args[1]
        for key in all_obj:
            if key is update_key:
                selected_obj_dict = all_obj[key]
                if args[2] in selected_obj_dict:
                    cast = type(selected_obj_dict[args[2]])
                    selected_obj_dict[args[2]] = cast(args[3])
                else:
                    select_obj_dict.update({args[2]: args[3]})


if __name__ == '__main__':
    HBNBCommand().cmdloop()
