#!/usr/bin/python3
"""the best console"""
import cmd
from models.user import User
from models.base_model import BaseModel
from models import storage

_dict = {BaseModel, User}


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        name = args
        clase = ["BaseModel", "User"]
        if name not in clase:
            print("** class doesn't exist **")
            return
        if name in clase:
            if name in _dict:
                new_instance = _dict(args)
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """Prints the string of an instance based on the class name"""

        arg = args.split()
        if len(arg) == 0:
            print("* class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = arg[0] + '.' + arg[1]
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = arg[0] + '.' + arg[1]
            objects = storage.all()
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name."""

        arg = args.split()
        if len(arg) > 0 and arg[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            print(objects)

    def do_update(self, args):
        """Updates an instance based on the class name and
        id by adding or updating attribute"""

        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif len(arg) >= 2:
            key = arg[0] + '.' + arg[1]
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                if key in objects:
                    setattr(objects[key], str(arg[2]), str(arg[3]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
